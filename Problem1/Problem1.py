s_emp = (('ID', 'LAST_NAME', 'FIRST_NAME', 'USERID', 'START_DATE', 'COMMENTS', 'TITLE', 'SALARY', 'COMMISSION', 'DEPT_ID', 'MANAGER_ID'),
         (1, 'MARTIN', 'CARMEN', 'MARTINCU', '3-MAR-90', '', 'PRESIDENT', 4500, 0, 50, 0),
         (10, 'JACKSON', 'MARTA', 'JACKSOMT', '27-FEB-91', '', 'WAREHOUSE MANAGER', 1507, 0, 45, 2),
         (11, 'HENDERSON', 'COLIN', 'HENDERCS', '14-MAY-90', '', 'SALES REPRESENTATIVE', 1400, 10, 31, 3),
         (12, 'GILSON', 'SAM', 'GILSONSJ', '18-JAN-92', '', 'SALES REPRESENTATIVE', 1490, 12.5, 32, 3),
         (13, 'SANDERS', 'JASON', 'SANDERJK', '18-FEB-91', '', 'SALES REPRESENTATIVE', 1515, 10, 33, 3),
         (14, 'DAMERON', 'ANDRE', 'DAMEROAP', '9-OCT-91', '', 'SALES REPRESENTATIVE', 1450, 17.5, 35, 3),
         (15, 'HARDWICK', 'ELAINE', 'HARDWIEM', '7-FEB-92', '', 'STOCK CLERK', 1400, 0, 41, 6),
         (16, 'BROWN', 'GEORGE', 'BROWNGW', '8-MAR-90', '', 'STOCK CLERK', 940, 0, 41, 6),
         (17, 'WASHINGTON', 'THOMAS', 'WASHINTL', '9-FEB-91', '', 'STOCK CLERK', 1200, 0, 42, 7),
         (18, 'PATTERSON', 'DONALD', 'PATTERDV', '6-AUG-91', '', 'STOCK CLERK', 795, 0, 42, 7),
         (19, 'BELL', 'ALEXANDER', 'BELLAG', '26-MAY-91', '', 'STOCK CLERK', 850, 0, 43, 8),
         (2, 'SMITH', 'DORIS', 'SMITHDJ', '8-MAR-90', '', 'VP, OPERATIONS', 2450, 0, 41, 1),
         (20, 'GANTOS', 'EDDIE', 'GANTOSEJ', '30-NOV-90', '', 'STOCK CLERK', 800, 0, 44, 9),
         (21, 'STEPHENSON', 'BLAINE', 'STEPHEBS', '17-MAR-91', '', 'STOCK CLERK', 860, 0, 45, 10),
         (22, 'CHESTER', 'EDDIE', 'CHESTEEK', '30-NOV-90', '', 'STOCK CLERK', 800, 0, 44, 9),
         (23, 'PEARL', 'ROGER', 'PEARLRG', '17-OCT-90', '', 'STOCK CLERK', 795, 0, 34, 9),
         (24, 'DANCER', 'BONNIE', 'DANCERBW', '17-MAR-91', '', 'STOCK CLERK', 860, 0, 45, 7),
         (25, 'SCHMITT', 'SANDRA', 'SCHMITSS', '9-MAY-91', '', 'STOCK CLERK', 1100, 0, 45, 8),
         (3, 'NORTON', 'MICHAEL', 'NORTONMA', '17-JUN-91', '', 'VP, SALES', 2400, 0, 31, 1),
         (4, 'QUENTIN', 'MARK', 'QUENTIML', '7-APR-90', '', 'VP, FINANCE', 2450, 0, 10, 1),
         (5, 'ROPER', 'JOSEPH', 'ROPERJM', '4-MAR-90', '', 'VP, ADMINISTRATION', 2550, 0, 50, 1),
         (6, 'BROWN', 'MOLLY', 'BROWNMR', '18-JAN-91', '', 'WAREHOUSE MANAGER', 1600, 0, 41, 2),
         (7, 'HAWKINS', 'ROBERTA', 'HAWKINRT', '14-MAY-90', '', 'WAREHOUSE MANAGER', 1650, 0, 42, 2),
         (8, 'BURNS', 'BEN', 'BURNSBA', '7-APR-90', '', 'WAREHOUSE MANAGER', 1500, 0, 43, 2),
         (9, 'CATSKILL', 'ANTOINETTE', 'CATSKIAW', '9-FEB-92', '', 'WAREHOUSE MANAGER', 1700, 0, 44, 2))

s_dept = (('ID','NAME', 'REGION_ID'),
        (10, 'FINANCE', 1),
        (31, 'SALES', 1),
        (32, 'SALES', 2),
        (33, 'SALES', 3),
        (34, 'SALES', 4),
        (35, 'SALES', 5),
        (41, 'OPERATIONS', 1),
        (42, 'OPERATIONS', 2),
        (43, 'OPERATIONS', 3),
        (44, 'OPERATIONS', 4),
        (45, 'OPERATIONS', 5),
        (50, 'ADMINISTRATION', 1)
        )

# 1. select * from s_dept;
print s_dept[1::]

# 2.select last_name, first_name, title, salary from s_emp;
print "\nselect Lname, Fname, title, sal from s_emp: ", [[i[1], i[3],i[6],i[7]] for i in s_emp[1::]]

# 3. select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40;
print "\nselect Lname, Fname, title, sal from s_emp where sal > 1500 and dept_id > 40: ", [[i[1], i[3],i[6],i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40]

# 4. select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name;
print "\nselect Lname, Fname, title, sal from s_emp where sal > 1500 and dept_id > 40 order by Lname: ", sorted([[i[1], i[3],i[6],i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40], key = lambda x: x[0])

# 5. select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc;
print "\nselect Lname, Fname, title, sal from s_emp where sal > 1500 and dept_id > 40 order by sal desc: ", sorted([[i[1], i[3], i[6],i[7]] for i in s_emp[1::] if i[5] > 1500 and i[9] > 40], key = lambda x: int(x[3]), reverse=True)

# 6. select last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id);
print "\nselect Lname, Fname, title, sal from s_emp e join s_dept d on(e.deptid = d.deptid): ", [[i[1], i[3], i[6],i[7],j[1]] for i in s_emp[1::] for j in s_dept[1::] if i[9] == j[0] ]

# 7. select dept_id, avg(salary) from s_emp group by dept_id order by dept_id;
print "\nselect deptid, avg(sal) from emp group by deptid order by deptid"
for department in { d[9] for d in s_emp[1::] }: (lambda deptno, avgSal: [deptno, avgSal])(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in s_emp[1::] if e[9] == department ])))

# 8. select dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500;
print "\nselect deptid, avg(sal) from s_emp group by deptid having avg(sal) < 1500"
print filter(None,[(lambda deptno, avgSal:[deptno,avgSal] if (avgSal < 1500) else None)(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in s_emp[1::] if e[9] == department ])))for department in { d[9] for d in s_emp[1::] } ])
