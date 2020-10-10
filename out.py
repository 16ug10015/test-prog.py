with open('inpfile.txt', 'r') as file:
    data = file.read().replace('\n', ',')
    data = data.replace(',,Goodies and Prices:,', '')
    data = data.replace('Number of employees','N')
    data = data.replace(': ',' - ')

d = {}
d = dict((k, int(v)) for k, v in (e.split(' - ') for e in data.split(',')))

values_view = d.values()
value_iterator = iter(values_view)
first_value = next(value_iterator)

new_dict = {k: d[k] for k in d.keys() - {'N'}}

n=len(new_dict)
namelist=[]
picelist=[]

p=[]
q=[]

for key, value in new_dict.items():
	temp1= key
	temp = value
	namelist.append(temp1)
	picelist.append(temp)

def minDiff(picelist,n,first_value):
    result = +2147483647
    picelist.sort() 
    for i in range(n-first_value+1):
    	x=picelist[i+first_value-1]
    	result = int(min(result, picelist[i+first_value-1] - picelist[i]))
    p.append(picelist[i+first_value-1])
    q.append(picelist[i])
    print(p)
    print(q)	 
    return result

print(minDiff(picelist, n, first_value)) 


