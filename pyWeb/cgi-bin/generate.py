import glob
import model
import yate

data_files = glob.glob("../data/*.txt")
img_dic = model.writeList(data_files)


print (img_dic)


print (yate.start_response())
print (yate.include_header("haha"))
print (yate.start_form("by my CGI"))
print (yate.para("from my data list"))
for item in img_dic:
    print(yate.radio_button("which_img",img_dic[item] ))
print(yate.end_form("Selec"))
print(yate.include_footer({"HOME": "/index.html"}))

