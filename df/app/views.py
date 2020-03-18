from django.shortcuts import render
import csv

def process_view(request):
    if request.method == "POST":
       user_data = request.POST.get('user_data')
       dict = {}
       sort_dict = {}
       l = []

       with open(r'app\example\abstracts_trainingset.csv', encoding='utf8') as csvfile:
           readCSV = csv.reader(csvfile, delimiter=',')

           for row in readCSV:
               count = 0
               for word in user_data.split():
                   if word in row[1].lower():
                       count += 1
                       dict[row[0]] = count
           if not dict:
               print("No matches")
           else:
               sort_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)[:10]}
               print(type(sort_dict))
               print(sort_dict)


               # for new_line in sort_dict:
               for k in sort_dict:
                   l.append(k)


       return render(request, 'base.html', {'title': l})
    else:
        return render(request, 'base.html')




