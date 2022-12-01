from . import views
from . import app

# urls for posts
app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
app.add_url_rule('/employee/create', view_func=views.employee_create, methods=['GET', 'POST'], endpoint='employee_create')
app.add_url_rule('/employee/<int:employee_id>', view_func=views.employee_detail, methods=['GET'], endpoint='employee_detail')
app.add_url_rule('/employee/<int:employee_id>/delete', view_func=views.employee_delete, methods=['GET', 'POST'], endpoint='employee_delete')
app.add_url_rule('/employee/<int:employee_id>/update', view_func=views.employee_update, methods=['GET', 'POST'], endpoint='employee_update')


# urls for user

app.add_url_rule('/register', view_func=views.register_view, methods=['GET', 'POST'], endpoint='register')
app.add_url_rule('/login', view_func=views.login_view, methods=['GET', 'POST'], endpoint='login')
app.add_url_rule('/logout', view_func=views.logout_view, methods=['GET'], endpoint='logout')
