article = 1
favorite = 2
history = 3
user = 4
disease = 5

article_error_map = {
    1: "Article not found",
    2: "Article already exists",
    3: "Article creation failed",
    4: "Article update failed",
    5: "Article deletion failed"
}

favorite_error_map = {
    1: "User or Article not found",
    2: "Favorite deletion failed"
}

history_error_map = {
    1: "User or Article not found",
    2: "History deletion failed"
}

user_error_map = {
    1: "User already exists",
    2: "User not found",
    3: "User creation failed",
    4: "User update failed",
    5: "User deletion failed",
    6: "Password or username is incorrect",
}

disease_error_map = {
    1: "Disease not found",
    2: "Disease already exists",
    3: "Disease creation failed",
    4: "Disease update failed",
    5: "Disease deletion failed"
}


def error_translate(moduel: int, code: int):
    if moduel == article:
        return article_error_map[code]
    if moduel == favorite:
        return favorite_error_map[code]
    if moduel == history:
        return history_error_map[code]
    if moduel == user:
        return user_error_map[code]
    if moduel == disease:
        return disease_error_map[code]
    return "Unknown error"
