from logging import debug
from flask import Flask, render_template, request 
import utils  
from utils import preprocessdata 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 

@app.route('/predict/', methods=['GET', 'POST'])


def predict():  
    if request.method == 'POST': 
        vintage = request.form.get('vintage')
        age = request.form.get('age')
        dependents = request.form.get('dependents')
        city = request.form.get('city')
        branch_code = request.form.get('branch_code')
        current_balance = request.form.get('current_balance')
        previous_month_end_balance = request.form.get('previous_month_end_balance')
        average_monthly_balance_prevQ = request.form.get('average_monthly_balance_prevQ') 
        average_monthly_balance_prevQ2 = request.form.get('average_monthly_balance_prevQ2') 
        current_month_credit = request.form.get('current_month_credit') 
        previous_month_credit = request.form.get('previous_month_credit') 
        current_month_debit = request.form.get('current_month_debit') 
        previous_month_debit = request.form.get('previous_month_debit') 
        current_month_balance = request.form.get('current_month_balance')
        previous_month_balance = request.form.get('previous_month_balance')
        doy_ls_tran = request.form.get('doy_ls_tran')
        woy_ls_tran = request.form.get('woy_ls_tran')
        moy_ls_tran = request.form.get('moy_ls_tran')
        dow_ls_tran = request.form.get('dow_ls_tran')
        gender_Male = request.form.get('gender_Male')
        occupation_retired = request.form.get('occupation_retired')
        occupation_salaried = request.form.get('occupation_salaried')
        occupation_self_employed = request.form.get('occupation_self_employed')
        occupation_student = request.form.get('occupation_student')
        customer_nw_category_2 = request.form.get('customer_nw_category_2')  
        customer_nw_category_3 = request.form.get('customer_nw_category_3')  
        
    prediction = utils.preprocessdata(vintage,age,dependents,city,branch_code,current_balance,previous_month_end_balance,average_monthly_balance_prevQ,average_monthly_balance_prevQ2,current_month_credit,previous_month_credit,current_month_debit,previous_month_debit,current_month_balance,previous_month_balance,doy_ls_tran,woy_ls_tran,moy_ls_tran,dow_ls_tran,gender_Male,occupation_retired,occupation_salaried,occupation_self_employed,occupation_student,customer_nw_category_2,customer_nw_category_3)

    return render_template('predict.html', prediction=prediction) 

if __name__ == '__main__':
	app.run(debug=True)
