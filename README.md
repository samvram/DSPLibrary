# Using DSPLibrary
DSPLibrary is a custom pythonlibrary created for tackling
practical problems faced in DSP courses for Engineering. We 
build this library for usage and development by students of **IIST**
for **AV311(Digital Signal Processing)**. The library is made for
**python**, for its open source usage. Yes, we promote *FOSS*.

##Setting up the environment
You need to have a working Python version installed on your system, along with 
*Numpy* and *Scipy* libraries installed. We will walk through the steps to install
this build on your system.

### Installing Python
On Windows OS, [download](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe)
 from this link and follow the installer for 
completing the installation.

Linux distributions usually have inbuilt Python support.

### Getting NumPy and SciPy

On Windows, setting the development environment is takes longer as it involves installing built binaries for `Numpy`, `Scipy`.
First download the binaries from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/). Then navigate to the folder where the `.whl` files
have been downloaded, and run the following (make sure you run them in the SAME ORDER as listed below from GIT Scm)
```bash
$ pip install numpyXXXX.whl
$ pip install scipyXXXX.whl
$ pip install matplotlib
```

On Ubuntu, simply run the following from the terminal
```bash
$ pip install numpy
$ pip install scipy
$ pip install matplotlib
```
### Getting the Library
In your standard **GIT** command line enter the following command
to get a copy
```bash
$ git clone https://github.com/samvram/DSPLibrary
```

### Using the library
Now that you have undergone the pain of installing the whole thing.
It is just for you to use and witness the power of DSP.

* DiscreteSignals is a class housing all the common signals you can 
use in your code to construct something
* DspToolKit is a library housing functions involving simple DSP operations,
at present we can demonstrate working with an example from a code

```python
# Import the required classes to use
from discretesignals import DiscreteSignals
from dsptoolkit import DspToolKit

# Create objects of both the classes to use
disc = DiscreteSignals()
dtk = DspToolKit()

# Create a time array starting from -5 to +5
#  using step size of 1
time = dtk.array_creator(-5,5,1)

# Create a step function(mappig) on the time axis 
# you created
func = disc.heaviside(time)
# Command to plot the function
dtk.plot(func)

func = disc.impulse(time, -2)
dtk.plot(func)

# Essential line to set visibility of the graphs
dtk.show()
```