from fastapi import APIRouter, UploadFile
from starlette.responses import FileResponse
from datetime import datetime
router = APIRouter(prefix='/file')


@router.post('/')
async def upload(file: UploadFile, user_id: int):
    if file.content_type.split('/')[0] != 'image':
        return -1
    now = datetime.now().timestamp()
    file_name = f'{user_id}'+'_' + \
        f'{now}.'+file.content_type.split('/')[1]
    path = r'./files/'+file_name
    with open(path, 'wb') as buffer:
        buffer.write(file.file.read())
    return r'http://127.0.0.1:8000/static/'+file_name

@router.get('/')
async def get_file(file_name: str):
    return FileResponse(r'./files/'+file_name, filename=file_name)
