from django.shortcuts import render, get_object_or_404, redirect
from .models import Credential, CustomerGeneral
from .forms import AddVTYCredentialsForm, CustomerGeneralForm
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError

# Create your views here.


@login_required
def settings_home(request):
    credentials = Credential.objects.all()
    general = get_object_or_404(CustomerGeneral, pk=1)
    error = ""
    context = {
        'credentials': credentials,
        'general': general,
        'page': 'General',
        'error': error
    }
    if request.method == "GET":
        return render(request, 'settings/settings_home.html', context)
    else:
        # Instantiate a form using the returned data.
        form = CustomerGeneralForm(request.POST)
        if form.is_valid():
            # Put this in DB, but don't save.
            newform = form.save()
            error = "Customer data saved successfully."
        else:
            error = "Error in the form.  Please correct and try again."
        return render(request, "settings/settings_home.html", context)


@login_required
def addvtycredential(request):
    # Create error based on validation of username and password.
    error = ""
    # track for a valid return.  if valid, then save to database.
    valid_return = True
    # Get list of credentials from DB for comparison.
    credentials = Credential.objects.all()
    if request.method == "GET":
        return render(request, "settings/add-vty.html")
    else:
        error, credential_pk = validatecredentials(request)
        if credential_pk != 0:
            credential = get_object_or_404(Credential, pk=credential_pk)
        else:
            credential = ""
        context = {
            'credential': credential,
            'error': error
        }
        return render(request, 'settings/add-vty.html', context)


@login_required
def editvtycredential(request, credential_pk):
    if request.method == "GET":
        credential = get_object_or_404(Credential, pk=credential_pk)
        context = {
            'credential': credential
        }
        return render(request, "settings/add-vty.html", context)
    else:
        error, credential_pk = validatecredentials(request)
        credential = get_object_or_404(Credential, pk=credential_pk)
        context = {
            'credential': credential,
            'error': error
        }
        return render(request, 'settings/vty/' + str(credential_pk) + 'edit/', context)


@login_required
def deletevtycredential(request, credential_pk):
    credential = get_object_or_404(Credential, pk=credential_pk)
    credentials = Credential.objects.all()
    error = ""
    if request.method == 'GET':
        deleted_username = credential.username
        try:
            credential.delete()
            error = deleted_username + " has been deleted from the database."
        except ProtectedError:
            error = deleted_username + " is being used by devices.  It cannot be deleted."
        context = {
            'credentials': credentials,
            'error': error,
            'page': 'Credentials'
        }
        return render(request, 'settings/settings_home.html', context)


@login_required
def addsnmpcredential(request):
    return render(request, "settings/add-snmp.html")


@login_required
def editsnmpcredential(request):
    return render(request, "settings/add-snmp.html")


@login_required
def deletesnmpcredential(request):
    return render(request, "settings/add-snmp.html")


def validatecredentials(request):
    # Get list of credentials from DB for comparison.
    credentials = Credential.objects.all()
    valid_return = True

    # Check if VTY passwords exist
    if request.POST['password'] == request.POST['password2']:

        # Get the list of devices so we can compare the IP to see if it already exists.

        returned_username = request.POST['username']
        returned_password = request.POST['password']
        for credential in credentials:
            # Check if returned username is equal to any credentials in the database.
            if credential.username == returned_username:
                # Check if returned password is ALSO equal to any credentials in the database.
                if credential.password == returned_password:
                    error = "This username/password combination already exists. Try again."
                    # Fail function
                    valid_return = False
    else:
        error = "VTY passwords do not match.  Try again."
        valid_return = False

    # Check the returned enable passwords to see if they match.
    if request.POST['enable_pass'] != request.POST['enablepassword2']:
        error = "Enable passwords do not match.  Please try again."
        valid_return = False

    # Instantiate a form using the returned data.
    form = AddVTYCredentialsForm(request.POST)

    # If we have a unique username/password combo, save to the database.
    if valid_return:
        if form.is_valid():
            # Put this in DB, but don't save.
            newform = form.save(commit=False)
            # Add user info to the form before saving.
            newform.user = request.user
            # Save the database if we received a valid input in the form.
            newform = newform.save()
            description = ""
            if newform.description:
                description = " - (" + newform.description + ")"
            error = "Added " + newform.username + description +  \
                    " to the database.  Add another, or close window."
            # Return error (or success) and ID of the new form
            return error, newform.id
        else:
            error = "Form is not valid.  Try again."
            return error, 0
    else:
        return error, 0


