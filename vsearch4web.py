from flask import Flask,render_template,request,redirect,escape
import vsearch
app = Flask(__name__)




@app.route('/search4',methods = ['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(vsearch.search4letters(phrase,letters))
    log_request(request,results)
    return render_template('result.html',the_title = title,
                                        the_phrase =phrase,
                                        the_letters = letters,
                                        the_results = results)
@app.route('/')   
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')

@app.route('/viewlog')
def viewlog_page():
    
    with open('vsearch.log') as log:
        contents=[]
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))

    the_title = 'View Log'
    the_row_titles = ['Form Data','Remote_addr','User_agent','Result']
    return render_template('viewlog.html',the_title = the_title,
                                            the_row_titles = the_row_titles,
                                            the_data = contents)

# @app.route('/results')
# def results_page():
#     return render_template('results.html', the_phrase = , the_letters= , the_title = 'Here are your resutls:' )
def log_request(req:'falsk_request',res:str):
    file_name = 'vsearch.log'
    with open(file_name,'a') as file_obj:
        print(req.form,req.remote_addr,req.user_agent,res,file = file_obj,sep = '|')
        

   



if __name__ == '__main__':
    app.run(debug = True)