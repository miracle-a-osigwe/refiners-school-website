from mcq.models import Assessment

def assessment_processor(request):
    assessment = Assessment.objects.all()
    return {'list_assessment' : assessment}