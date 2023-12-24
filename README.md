<!DOCTYPE html>
<html>
<head>
</head>
<body>

<h1>beat_wordle</h1>
A simple python code to beat New York Time's wordle puzzle

<h2>How to use this to beat today's wordle</h2>
<ol type="1">
  <li>Start with any 5 letter word. Any word that comes to your mind. Do not worry if none of the letters are matches. See what you get.</li>
  <li>Enter the information about your attempt in hints.csv file.<br>
  <ul>  
    <li>Enter "TRUE" without quotes against the letter under column "Omit" if the letter is absent (<span style="color:#777A7C">grey</span> as per game's hint)</li>
    <li>Enter the position of <span style="color:#79A86B">green</span> letters under "True Position" column</li>
    <li>Enter the position of <span style="color:#C4B465">yellow</span> letters under "False Position" column</li>
    <li>Save the file</li>
  </ul>
  <li>Open the python code</li>
  <li>Install the packages if you do not have them</li>
  <li>Change file path according to where your hints.csv file is in line 24</li>
  <li>Save and run the python code. Python will print a list of words for you to try. Select any one of them and try that on wordle puzzle</li>
  <li>If you are not 100% correct, you will have new information on which letters are guessed right/ wrong. Enter this information like in step 2 and continue on till step 7 until guessed the right word. Do not worry, you will always get to the right word in <6 tries. I usually get it right in 3-4 tries on average.</li>
</ol>


</body>
</html>

