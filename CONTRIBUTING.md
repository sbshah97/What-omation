#How to contribute

Our project is opened for contributions, and we are always happy to welcome best pieces of code from the Github community. So, **here are some ways you can help us**:

- [Feature requests] (#feature)
- [Bug reports] (#bug)
- [Pull requests] (#pull)
- [More information] (#info)


## <a name="feature"></a> Time for new features

You can request a new feature by submitting an issue to our [Github Repository][github].


## <a name="bug"></a> Bug reports

A bug is a *demonstrable problem* that is caused by the code in the repository. Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

1. **Use the GitHub issue search**. Check if the issue has already been reported.

2. **Check if the issue has been fixed**. Try to reproduce it using the latest master or development branch in the repository.

3. **Provide environment details**. Provide your operating system, browser(s), devices, and jquery-asScrollbar version.

4. **Create an isolated and reproducible test case**. Create a reduced test case.

5. **Include a live example**. Make use of jsFiddle or jsBin to share your isolated test cases.

A good bug report shouldn't leave others needing to chase you up for more information. Please try to be as detailed as possible in your report.

* What is your environment?
* What steps will reproduce the issue?
* What browser(s) and OS experience the problem?
* What would you expect to be the outcome?
**All these details** will help people to fix any potential bugs.

###Example:

>Short and descriptive example bug report title
>A summary of the issue and the browser/OS environment in which it occurs. If suitable, include the steps required to reproduce the bug.

>This is the first step
This is the second step
Further steps, etc.
<url> - a link to the reduced test case

Any other information you want to share that is relevant to the issue being reported. This might include the lines of code that you have identified as causing the bug, and potential solutions (and your opinions on their merits).

##<a name="pull"></a>Pull requests
* Include screenshots and animated GIFs in your pull request whenever possible.
* Follow the _JavaScript_ and _CoffeeScript_ styleguides.
* Include thoughtfully-worded, well-structured Jasmine specs in the ./spec folder. Run them using 'apm test'.
* Document new code based on the _Documentation Styleguide_
* End files with a newline.
* Place requires in the following order:
* Built in Node Modules (such as path)
* Place class properties in the following order:
    * Class methods and properties (methods starting with a @)
    * Instance methods and properties
* Avoid platform-dependent code:
    * Use `require('fs-plus').getHomeDirectory()` to get the home directory.
    * Use `path.join()` to concatenate filenames.
    * Use `os.tmpdir()` rather than '/tmp' when you need to reference the temporary directory.


##<a name='info'></a>More information
You can find out more detailed information about contributing in the [WhatsApp-web documentation][Readme]


[readme]: https://github.com/salman-bhai/WhatsApp-web/blob/master/README.md
[github]: https://github.com/salman-bhai/WhatsApp-web

