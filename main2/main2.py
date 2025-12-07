from pyscript import display, document

def general_weighted_average(e):
    # Clear previous outputs
    document.getElementById('student_info').innerHTML = ''
    document.getElementById('summary').innerHTML = ''
    document.getElementById('output').innerHTML = ''

    # Subject names and corresponding unit weights
    subjects = ['Anatomy', 'Physiology', 'Pathology', 'Biochem', 'Genetics', 'Microbiology']
    units_subject = (6, 5, 4, 3)

    # Get input values
    given_name = document.getElementById('given_name').value
    surname = document.getElementById('surname').value

    anatomy = float(document.getElementById('anatomy').value or 0)
    physiology = float(document.getElementById('physiology').value or 0)
    pathology = float(document.getElementById('pathology').value or 0)
    biochem = float(document.getElementById('biochem').value or 0)
    genetics = float(document.getElementById('genetics').value or 0)
    microbiology = float(document.getElementById('microbiology').value or 0)

    # Compute weighted sum and total units
    weighted_sum = (
        anatomy * units_subject[0] +
        physiology * units_subject[0] +
        pathology * units_subject[1] +
        biochem * units_subject[1] +
        genetics * units_subject[2] +
        microbiology * units_subject[3]
    )

    total_units = (units_subject[0] * 2) + (units_subject[1] * 2) + units_subject[2] + units_subject[3]
    gpa = weighted_sum / total_units

    # Summary text
    summary = f"""
    {subjects[0]}: {anatomy:.0f}
    {subjects[1]}: {physiology:.0f}
    {subjects[2]}: {pathology:.0f}
    {subjects[3]}: {biochem:.0f}
    {subjects[4]}: {genetics:.0f}
    {subjects[5]}: {microbiology:.0f}
    """

    # Display results
    display(f'Name: {given_name} {surname}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gpa:.2f}', target='output')
