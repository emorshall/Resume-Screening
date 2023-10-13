import dateutil.utils
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, ResumeProfileForm, SkillsForm, CandidateForm
from .models import Login, ResumeProfile, Skills, CandidateProfile
import json
from resumeConverter import ResumeScreening


# Create your views here.

user = ""
def dashboard(request):
    return render(request, "home.html", {"user": "Prabhu"})


def home(request):
    return render(request, "login.html", {"message": "Login"})


def register(request):
    return render(request, "register.html", {})


def resumeCategory(request):
    resumeProfile = {
        'profile_data': ResumeProfile.objects.all(),
        'skill_data': Skills.objects.all(),
    }
    return render(request, "tables.html", resumeProfile)


def signUpAction(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # getLoginTable = Login.get_latest_by()
            print(f'get username: ' + form.cleaned_data['name'])
            print(f'get password: ' + form.cleaned_data['password'])
            return redirect('login')
        else:
            form = LoginForm()
            return render(request, 'register.html', {})


def loginAction(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['name']
        password = form.cleaned_data['password']
        if validateUser(username, password):
            global user
            user = username
            return render(request, "home.html", {"user": username})
        else:
            return render(request, 'login.html', {"message": "Invalid User ! Please Retry"})


def validateUser(username, password):
    validate = False
    getLoginTable = Login.objects.all()
    for val in getLoginTable:
        if (username == val.name) & (password == val.password):
            validate = True
            break
    return validate


def resumeProfiling(request):
    if request.method == "POST":
        form = ResumeProfileForm(request.POST)
        if form.is_valid():
            getData = ResumeProfile(
                profile_name=form.cleaned_data['profile_name'],
                profile_keyword=",".join(request.POST.getlist('profile_keyword')),
                active=form.cleaned_data['active'],
            )
            getData.save()
        return redirect('category')
    else:
        return render(request, 'tables.html', {})


def updateProfile(request):
    mylist = request.POST.getlist('active[]')
    print(mylist)
    return None


def Screening(request):
    resumeProfile = {
        'profile_list': ResumeProfile.objects.all(),
        'candidate_data': CandidateProfile.objects.filter(active=True),
        'message': False,
        'user': user
    }
    return render(request, "screening.html", resumeProfile)


def resumeScreening(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        getFile = request.FILES['file']
        profile_name = request.POST['profile_name']
        skills = ResumeProfile.objects.filter(profile_name=profile_name)
        skillList = skills[0].profile_keyword.split(',')
        candidateResult = ResumeScreening(getFile, skillList)
        candidate_contact_exit = CandidateProfile.objects.filter(can_contact=candidateResult['phone_num'])
        candidate_email_exit = CandidateProfile.objects.filter(can_contact=candidateResult['email_id'])
        if (candidate_email_exit.exists()) or (candidate_contact_exit.exists()):
            resumeProfile = {
                'profile_list': ResumeProfile.objects.all(),
                'candidate_data': CandidateProfile.objects.filter(active=True),
                'message': True
            }
            return render(request, "screening.html", resumeProfile)

        else:
            if form.is_valid():
                print("inside form")
                print(form.cleaned_data['can_name'])
                print(str(candidateResult['skills']))
                print(candidateResult['result_in_per'])
                print(candidateResult['email_id'])
                print(candidateResult['phone_num'])
                setCanProfile = CandidateProfile(
                    can_name=form.cleaned_data['can_name'],
                    can_email=candidateResult['email_id'],
                    can_contact=candidateResult['phone_num'],
                    can_skills=str(candidateResult['skills']),
                    can_status=candidateResult['result_in_per'],
                    created_date=dateutil.utils.today(),
                    active=True,
                )
                setCanProfile.save()
                return redirect('screen')
            else:
                return render(request, 'screening.html', {})
    else:
        return render(request, 'screening.html', {})


def skills(request):
    skillList = Skills.objects.all()
    # skillJson = json.dumps(skillList)
    skillJson = serialize("json", skillList)
    serialized_data = json.loads(skillJson)
    skills = {
        'skill_data': skillList,
        'skill_json': serialized_data
    }
    return render(request, "skills.html", skills)


def skillSubmit(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            skillName = form.cleaned_data['skill_name'].lower()
            getData = Skills(
                skill_name=skillName,
                active=form.cleaned_data['active'],
            )
            getData.save()
        return redirect('skills')
    else:
        return render(request, 'skills.html', {})
