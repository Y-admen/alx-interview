# Star Wars API

## Parse Command Line Arguments in Node.js
 using **process.argv** and with **yargs** and **minimist**

 ### using process.argv
 **First**, file system path pointing to the node executable.
**Second** the name of the JavaScript file that is being executed.
**Third**, the first argument that is passed by the user.

Example/

```javascript
'use strict';
for (let j = 0; j < process.argv.length; j++) {
    console.log(j + ' -> ' + (process.argv[j]));
}
// output
1
2
3
4
```
Now run ‘processargv.js’ using the following command by passing argument.
node processargv.js I am Node 

##  HTTP requests in Node
