from django.shortcuts import redirect

def redirect_view(request):
    # Determine the redirection URL based on user fields
    if request.user.is_authenticated:
        if request.user.userKind == 'patient':
            next_redirect = 'redirect/patient_dashboard/'
        else:
            next_redirect = 'redirect/doctor_dashboard/'

        # Redirect the user
        return redirect(next_redirect)

    return redirect('/accounts/login')