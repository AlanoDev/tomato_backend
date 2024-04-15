from tomato.web.utils.error_translate import error_translate


def handle_results(error: bool, msg: str, data: any, code: int):
    if error:
        return {
            "error": error_translate(code//10, code % 10),
            "code": code,
        }
    else:
        return {
            "code": code,
            "msg": msg,
            "data": data
        }
