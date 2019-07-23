##############
#
#  Installed memory profiler ( package)
#


from memory_profiler import profile


fp=open('memory_profiler.log','a+')

@profile(stream=fp)
def my_func():
    a = [1] * (10 ** 6)   ## This will add 10 to the power 6 times 1 into this list
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()



# Use mprof .py to sample the data
#use mprof plot then to plot the graph.


