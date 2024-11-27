from app.database import async_session_maker
from sqlalchemy import select, delete, update
from app.models.model import Posts

class PostsDAO:
    @classmethod
    async def find_by_id(cls, post_id: int):
        async with async_session_maker() as session:
            query = select(Posts).filter_by(id=post_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Posts)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def delete_post(cls, post_id: int):
        async with async_session_maker() as session:
            query = delete(Posts).where(Posts.id == post_id) 
            await session.execute(query)
            await session.commit()
            
    @classmethod
    async def upgrade_post(cls, id: int, text: str):
        async with async_session_maker() as session: 
            query = select(Posts).where(Posts.id == id)
            result = await session.execute(query)
            post_update = result.scalars().first()
            post_update.text = text.text
            await session.commit()
            return {"id": post_update.id, "text": post_update.text}
    
    @classmethod 
    async def get_like(cls, like_id: int, like: bool):
        async with async_session_maker() as session: 
            query = select(Posts).where(Posts.id == like_id)
            result = await session.execute(query)
            post = result.scalars().first()
            post.like = like
            await session.commit()
            return {"id": post.id, "text": post.text, "like": post.like}
    
    @classmethod
    async def get_new_post(cls, text: str, like: bool):
        async with async_session_maker() as session:
            new_post = Posts(text=text, like=like)  
            session.add(new_post)
            await session.commit() 
            return {"id": new_post.id, "text": new_post.text, "like": new_post.like}
            
        
    @classmethod
    async def delete_like_for_id(cls, post_id: int):
        async with async_session_maker() as session: 
            query = select(Posts).where(Posts.id == post_id)
            result = await session.execute(query)
            post = result.scalar_one_or_none()
            if post.like:
                stat = update(Posts).where(Posts.id == post_id).values(like=False)
                await session.execute(stat)
                await session.commit()
                