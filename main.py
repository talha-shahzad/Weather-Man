import os
import sys
month = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
}

nmonth = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

class Year_Data:
    def __init__(self):
        self.maxt = {'max_temp': float('-inf'), 'date': ''}
        self.mint = {'min_temp': float('inf'), 'date': ''}
        self.maxh = {'max_humid': float('-inf'), 'date': ''}
    def display(self):
        maxt= self.maxt['date'].split("-")
        mint= self.mint['date'].split("-")
        maxh= self.maxh['date'].split("-")
        print("\n---------------------------------------------------------------------------\n")
        print(f"Highest: {int(self.maxt['max_temp'])}C on {month[int(maxt[1])]} {maxt[2]}") 
        print(f"Lowest: {int(self.mint['min_temp'])}C on {month[int(mint[1])]} {mint[2]} ")
        print(f"Humid: {int(self.maxh['max_humid'])}% on {month[int(maxh[1])]} {maxh[2]} ")
        print("\n---------------------------------------------------------------------------\n")

class Graph_Data():
    def __init__(self):
        self.maxList=[]
        self.minList=[]


# Generator function to read the file in the folder based on the year
def read_file(year, folder):
    try:
        dir = os.getcwd() + "\\" + folder
        # Read the text file
        for file in os.listdir(dir):
            if year in file.split("_"):
                yield file
    except Exception as e:
        print("Error: please Check the File name \n", e)

def read_file_month(year, month, folder):
    try:
        dir = os.getcwd() + "\\" + folder
        # Read the text file
        for file in os.listdir(dir):
            if year in file.split("_") and month in file:
                yield file
    except Exception as e:
        print("Error: please Check the File name \n", e)




def populate_data(column,val,date,obj):
    if column == "Max TemperatureC":
        if val > obj.maxt['max_temp']:
            obj.maxt['max_temp'] = val
            obj.maxt['date'] = date

    elif column == "Min TemperatureC":
        if val < obj.mint['min_temp']:
            obj.mint['min_temp'] = val
            obj.mint['date'] = date

    elif column == "Max Humidity":
        if val > obj.maxh['max_humid']:
            obj.maxh['max_humid'] = val
            obj.maxh['date'] = date
    else:
        print("Column not found")

def get_col_name(header, column):
    for col in header:
            if col.strip() == column:
                index= header.index(col)
                break
    return index



def print_month_data(column,avg):
    

    if column == "Max TemperatureC":
        print(f"Highest Average: {int(avg)}C")
    elif column == "Min TemperatureC":
        print(f"Lowest Average: {int(avg)}C")
    elif column == "Max Humidity":
        print(f"Average Humidity: {int(avg)}%\n\n")
    else:
        print("Column not found")
    

def get_values(flist, column,index):
    tcol=[line[index] for line in flist][1:]
    tcol = [float(value) for value in tcol if value != ""]

    if 'Max' in column:
        maxv=max(tcol)
        maxind=tcol.index(max(tcol))
        return maxind, maxv
    else:
        minv=min(tcol)
        minind=tcol.index(min(tcol))
        return minind, minv

def get_avg_values(flist, column,index):
    tcol=[line[index] for line in flist][1:]
    tcol = [float(value) for value in tcol if value != ""]
    total_sum = sum(tcol)
    num_elements = len(tcol)
    avg = total_sum / num_elements
    return avg

def Graph(flist,index):
    tcol=[line[index] for line in flist][1:]
    tcol = [float(value) for value in tcol if value != ""]
    return tcol

def populate_Graph_data(lists, column,obj):
    if column == "Max TemperatureC":
        obj.maxList=lists
    elif column == "Min TemperatureC":
        obj.minList=lists


#-----------------------------------------------------------------------------
# Special Function to call other functions
def read_column(flist,column,obj,check):
    header = flist[0]
    index=get_col_name(header, column)
    if check==1:
        ind, val=get_values(flist, column,index)
        date=flist[ind+1][0]
        populate_data(column,val,date,obj)
    elif check==2:
        avg=get_avg_values(flist, column,index)
        print_month_data(column,avg)
    else:
        populate_Graph_data(Graph(flist,index), column,obj)





def FileExplorer(file_generator,obj,check):
    with open(folder + "\\" + filename) as file:
            flist=[line.strip().split(",") for line in file]
            if flist[0]==['']:
                flist=flist[1:-1]
            read_column(flist, "Max TemperatureC", obj,check)
            read_column(flist, "Min TemperatureC",obj,check)
            if check<3:
                read_column(flist, "Max Humidity",obj,check)
            file.close()    
    

if __name__=="__main__":
    print("Hello World")

    # Print the arguments passed to the script
    input_date = sys.argv[1]
    input_date=input_date.split("/")
    if len(input_date) > 1:
        inp_month = input_date[1]
        inp_month=nmonth[int(inp_month)]
    inp_year = input_date[0]
    
    folder = sys.argv[2]
    obj=Year_Data()
    

    file_generator = read_file(inp_year, folder )
    for filename in file_generator:
        FileExplorer(filename, obj, 1)
    obj.display()

    if len(input_date) > 1:
        file_generator = read_file_month(inp_year,inp_month, folder)
        filename=next(file_generator)
        FileExplorer(filename, obj, 2)

        graphObj=Graph_Data()
        FileExplorer(filename, graphObj, 3)
        count=1

        print('---------------------------------------------------------------------------\n')
        print(inp_month,inp_year)
        for i in zip(graphObj.maxList,graphObj.minList):
            x,y=i
            print(f"{count:02} \033[31m{'+'*int(x)}  \033[0m {int(x)}C\n")
            print(f"{count:02} \033[34m{'+'*int(y)}  \033[0m {int(y)}C\n")
            count+=1


    
    

       
    


