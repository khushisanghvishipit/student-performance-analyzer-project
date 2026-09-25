#Scholarship Eligiblity Module
def check_scholarship(percentage,status):
    """Check whether student is eligiblity for scholarship"""
    if status=="PASS" and percentage>=85:
        scholarship="Eligible"
        message="Student is  eligible for scholarship."
    else:
        scholarship="Not Eligible"
        message="Student is not eligible for scholarship."
    return scholarship,message

