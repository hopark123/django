#!/usr/bin/python3

def ft_tr(f, r):
	f.write("			<tr>\n")
	i = 0
	while i < 18:
		line = r.readline().strip()
		if not line: break
		line = ":".join(line.split('='))
		line = ",".join(line.split(':'))
		lst = line.split(',')
		while int(lst[2]) != i :
			ft_td(f, 0, 0)
			i += 1
		ft_td(f, lst, 1)
		i += 1
	f.write("			</tr>\n")

def ft_td(f, lst, flag) :
	f.write("				<td>\n")
	if (flag == 1) :
		f.write("					<h4>" + lst[0].strip() + "</h4>" + "\n")
		f.write("					<ul>\n")
		f.write("						<li>" + "No ." + lst[4].strip() + "</li>\n")
		f.write("						<li>" + lst[6].strip() + "</li>\n")
		f.write("						<li>" + "mol : " + lst[8].strip() + "</li>\n")
		f.write("						<li>" +  "electron<br>[" +lst[10].strip() + "]" + "</li>\n")
		f.write("					</ul>\n")
	f.write("				</td>\n")

def ft_table(f, r):
	f.write("		<table>\n")
	[ft_tr(f, r) for _ in range(7)]
	f.write("		</table>\n")

def ft_haed(f):
	f.write("	<head>\n")
	f.write("		<title>ex07</title>\n")
	f.write("		<style>\n")
	f.write("			table {\n")
	f.write("				border : 1px solid;\n")
	f.write("				border-collapse : collapse;\n")
	f.write("			}\n")
	f.write("			th, td {\n")
	f.write("				width : 500px;\n")
	f.write("				border : 1px solid;\n")
	f.write("			}\n")
	f.write("		</style>\n")
	f.write("	</head>\n")

def ft_body(f, r):
	f.write("	<body>\n")
	ft_table(f, r)
	f.write("	</body>\n")

def ft_all(f, r):
	f.write("<!DOCTYPE html>\n")
	f.write("<html lang=\"en\">\n")
	ft_haed(f)
	ft_body(f, r)
	f.write("</html>\n")

def main():
	f = open('periodic_table.html', mode='wt', encoding='utf-8')
	r = open('periodic_table.txt', mode='r', encoding='utf-8')
	ft_all(f, r)
	r.close()
	f.close()

if __name__ == '__main__':
	main()
