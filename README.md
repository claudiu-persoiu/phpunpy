phpunpy
=======

I’ve created this script because I couldn’t find a way of displaying the unserialized string in a similar fashion with the vardump function from PHP. Also a very important feature with this library is to work with serialised strings with invalid endings. Sometimes the end of a serialised output is trimed in the logs and is hard to reconstrituate the valid part of the structure.

This script is unserializing a string serialized using:


	$output = serialize($input);


The output is equivalent with:

	
	var_dump(unserialize($output));


USAGE
-----

Make sure to import the library:


	from unserializer.DumpPHPUnserialized import *
	
	
And just run the class like so:


	DumpPHPUnserialized(string_to_desirelise).unserialize()


The result is a string

DEMO
----

A demo that requires Tk can be run using:


	./unpy.py
	
	
or


	python unpy.py


DISCLAIMER

IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
