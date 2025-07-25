from clients.courses.courses_client import get_courses_client
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExercisesRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.course_schema import CreateCourseRequestSchema


# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema()
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
# create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Инициализируем клиенты
files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")

# Загрузить файл с помощью метода FilesClient.create_file (уже реализовано в данном уроке).
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

# Создать курс с помощью метода CoursesClient.create_course (уже реализовано в данном уроке).
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создать задание с помощью метода ExercisesClient.create_exercise (реализуется в рамках данного задания).

create_exercise_request = CreateExercisesRequestSchema(course_id=create_course_response.course.id)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print("Create exercise data", create_exercise_response)
# get_exercises_client() (реализуется в рамках данного задания).