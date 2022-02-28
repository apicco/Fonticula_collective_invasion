from matplotlib import pyplot as plt
import numpy as np

dt = 4.9 #s
d = np.transpose( np.loadtxt( 'Results.txt' , delimiter = ',' ) )
print( "max time: " + str( dt * ( 90 - min( d[ 0 ] ) ) ) )
stop = [ i * dt for i in  d[ 1 ] - d[ 0 ] ]
retraction = [ i * dt for i in  d[ 2 ] - d[ 1 ] ]
undefined = [ i * dt for i in  d[ 3 ] - d[ 1 ] ]
stampede = [ i * dt for i in  d[ 4 ] - d[ 1 ] ]

num_backward_events =  np.count_nonzero( ~np.isnan( retraction ) )
num_undefineds =  np.count_nonzero( ~np.isnan( undefined ) )
num_forward_events =  np.count_nonzero( ~np.isnan( stampede ) )

print( 'N backward events :' + str( num_backward_events ) )
print( 'N undefined events:' + str( num_undefineds ) )
print( 'N forward events:' + str( num_forward_events ) )
num_tot = num_backward_events + num_undefineds + num_forward_events
sizes = [ num_backward_events/num_tot * 100 , num_undefineds/num_tot * 100 , num_forward_events / num_tot * 100 ]

f , a = plt.subplots()
a.bar( ( 0 , 1 ) , ( sizes[ 0 ] , sizes[ 2 ] ) )
plt.ylabel( '%' )
plt.xticks( [ 0 , 1 ] , [ 'Backward' , 'Forward' ] )
plt.title( 'The percentage of snakes that move\nwthin 7 minutes from laser thickling' )
plt.savefig( 'bar.pdf' )
