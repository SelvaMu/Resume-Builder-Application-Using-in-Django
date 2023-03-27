from django.shortcuts import render
from django.http import HttpResponse
from . import models
from xhtml2pdf import pisa
from django.contrib import messages
from io import BytesIO
from django.template.loader import get_template


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


def home(request):
    return render(request, "user.html")

def generate(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name', '')
            mobile = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address', '')
            objective = request.POST.get('objective', '')
            institution = request.POST.getlist('institution', '')
            qualification = request.POST.getlist('qualification', '')
            year = request.POST.getlist('year', '')
            cgpa = request.POST.getlist('cgpa', '')
            skill = request.POST.getlist('skill', '')
            project = request.POST.getlist('project', '')
            experience = request.POST.getlist('experience', '')
            declaration = request.POST.get('declaration', '')
            resume = request.POST.get('resume', '')
            # print(resume)

            if resume=="0":

                context = {
                    'name': name,
                    'mobile': mobile,
                    'email': email,
                    'address': address,
                    'objective': objective,
                    'institution': institution,
                    'qualification': qualification,
                    'year': year,
                    'cgpa': cgpa,
                    'skill': skill,
                    'project': project,
                    'experience': experience,
                    'declaration':declaration
                }

                data = models.Resumedata(name=name, mobile=mobile, email=email, address=address, objective=objective, institution=institution, qualification=qualification,
                    year=year, percentage=cgpa, skill=skill, project=project, experience=experience, declaration=declaration)
                data.save()

                # Render the template with the form data
                pdf = render_to_pdf('resume1.html',{"context":context})

                response = HttpResponse(pdf, content_type='application/pdf')
                # filename = "Resume1.pdf"
                content = "attachment; filename=Resume1.pdf"
                response['Content-Disposition'] = content
                return response

            elif resume=="1":
                context = {
                    'name': name,
                    'mobile': mobile,
                    'email': email,
                    'address': address,
                    'objective': objective,
                    'institution': institution,
                    'qualification': qualification,
                    'year': year,
                    'cgpa': cgpa,
                    'skill': skill,
                    'project': project,
                    'experience': experience,
                    'declaration': declaration
                }

                data = models.Resumedata(name=name, mobile=mobile, email=email, address=address, objective=objective, institution=institution, qualification=qualification,
                    year=year, percentage=cgpa, skill=skill, project=project, experience=experience, declaration=declaration)
                data.save()

                pdf = render_to_pdf('resume2.html',{"context":context})

                response = HttpResponse(pdf, content_type='application/pdf')
                # filename = "Resume2.pdf"
                content = "attachment; filename=Resume2.pdf"
                response['Content-Disposition'] = content
                return response

                # return render(request, "resume2.html", {"context": context})

            else:
                print("Error")
        return HttpResponse("Invalid request method")
    except:
        messages.info(request,"Refresh Here")
        return render(request,'user.html')