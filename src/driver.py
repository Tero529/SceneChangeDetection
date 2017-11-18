import sys
import helpers as he
import csv
if sys.argv[1] == 'thresh':
    import thresh as solution
elif sys.argv[1] == 'histo':
    import histo as solution

(grey_frams,images) =he.parse(sys.argv[8])

if sys.argv[1] == 'thresh':
    changes = solution.detect(grey_frams,images,float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),float(sys.argv[7]))
elif sys.argv[1] == 'histo':
    coorelations = solution.detect(grey_frams)
    with open(sys.argv[9], 'wb') as myfile:
        #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr = csv.writer(myfile, delimiter=';', lineterminator='\n')
        for k in range(len(coorelations)):
            wr.writerow(coorelations[k])
#print 'Total Changes were '+ str(changes)
