from passlib.context import CryptContext


pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:

    def verify_password(plain_password: str, hashed_password: str):
        return pwd_ctx.verify(plain_password, hashed_password)


    def get_password_hash(password: str):
        return pwd_ctx.hash(password)
