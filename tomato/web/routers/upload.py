from fastapi import APIRouter,UploadFile
from datetime import datetime
import os
router = APIRouter(prefix='/upload')

@router.post('/')
async def upload(file: UploadFile,user_id:int):
    print(os.getcwd())
    if file.content_type.split('/')[0] != 'image':
        return -1
    now=datetime.now().timestamp()
    file_name=f'./files/{user_id}'+'_'+f'{now}.'+file.content_type.split('/')[1]
    with open(file_name, 'wb') as buffer:
        buffer.write(file.file.read())
    return file_name