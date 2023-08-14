from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Nature, Complain,Status, Customer
from django.contrib import messages

@login_required
def add(request):
    if request.method == 'POST':
        id_nature = request.POST.get('id_nature')
        description = request.POST.get('description')
        attached_file = request.FILES.get('attached_file')
       
        if id_nature and description:
            try:
                nature = Nature.objects.get(id_nature=id_nature)
               
                
                try:
                    customer = Customer.objects.get(email=request.user.email)
                   
                    # Retrieve the default status (assuming the first status has primary key 1)
                    default_status = Status.objects.get(pk=1)
                   
                    complain = Complain.objects.create(
                        account_number=customer,
                        id_nature=nature,
                        id_status=default_status,  
                        description=description,
                        attached_file=attached_file
                    )
                    messages.success(request, 'Complaint submitted successfully.')
                    return redirect('home')  
                except Customer.DoesNotExist:
                    messages.error(request, 'Customer not found.')
                   
            except Nature.DoesNotExist:
                messages.error(request, 'Invalid nature selection.')
        else:
            messages.error(request, 'Please fill in all required fields.')
   
    nature_options = Nature.objects.all()
    context = {'nature_options': nature_options}
    return render(request, 'complain/add.html', context)