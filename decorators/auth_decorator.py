from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admin privileges required.")
            # return None
        else:
            return func(user_role)
    return wrapper

@require_admin 
def access_admin_panel(role):
    print("Access granted: Welcome to the admin panel.")

access_admin_panel("user")  # Output: Access denied: Admin privileges required.
access_admin_panel("admin")  # Output: Access granted: Welcome to the admin panel.