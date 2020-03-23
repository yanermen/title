"""

For rendering

"""
from django.shortcuts import render

""""

Reading the csv file

"""
import csv

def process_view(request):
    """"

    We send the request after that we open the csv file, read and match user_data with the abstract part from file
    Finally all result we render on the html

    """
    if request.method == "POST":
       user_data = request.POST.get('user_data')
       dict = {}

       with open(r'app/example/abstracts_trainingset.csv', encoding='utf8') as csvfile:
           readCSV = csv.reader(csvfile, delimiter=',')

           for row in readCSV:
               count = 0
               for word in user_data.lower().split():
                   if word in row[1].lower():
                       count += 1
                       dict[row[0]] = count

           else:
               sort_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)[:10]}
               print(type(sort_dict))
               print(sort_dict)

               l = [k for k in sort_dict]
               if l == []:
                   l.append("No matches could you write it in more details, please")

       return render(request, 'base.html', {'title': l})
    else:
        return render(request, 'base.html')