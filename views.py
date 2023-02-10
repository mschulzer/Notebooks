from sklearn import model_selection
from sklearn.linear_model import LogisticRegression, LinearRegression
import pickle


def model_view(request):
    
    filename = 'model/tr_model.sav'
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, filename)
    
    loaded_model = pickle.load(open(file_path, 'rb'))
    
    # Init with default values
    my_data = [0, 0, 0, 0]
    result = 0
    weeks = 10
    days = 3
    selectIntensity = 0.70


    if request.method == 'POST':
        weeks = request.POST.get("weeks")
        days = request.POST.get("days")
        selectIntensity = request.POST.get("selectIntensity")
        
        my_data = [0, 0, 0, 0]
        my_data[0] = int(weeks)
        my_data[1] = int(days)
        my_data[2] = 2700
        my_data[3] = int(selectIntensity)/100
        
        result = loaded_model.predict([my_data])
        result = round(result[0], 2)

    return render(request, "model.html", { 'result': result })
