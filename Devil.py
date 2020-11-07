#!/usr/bin/env python
#-*-coding:utf-8-*-
# Devil By Aryan
<title>TikTok Followers</title>

<style>
body {
  background-color: #ff004f;
}
</style>

</head>
<body style = "text-align:center">
<h1 style = "color:green;">
</br>
Write a TikTok username here
</h1>
 <div class="box red"></div>
</br></br></br>

<input autofocus required pattern="[^' ']+" type = "text" placeholder="Username" autocomplete="on" id="myInput">
 <button type="button" onclick="getInputValue();">Get Value</button>

 <iframe id="myFrame" scrolling="no" src="https://www.realtimetiktok.com/?user=samthemans" style="border: 0px none; width: 1890px; height: 726px; overflow: hidden position: relative; left: -100px; top: -100px relative"> </iframe>
<script>
        function getInputValue(){
            // Selecting the input element and get its value 
            var inputVal = document.getElementById("myInput").value;
            let x = (inputVal);
    document.getElementById("myFrame").src = "https://www.realtimetiktok.com/?user=" + x;
}

 </script>
</body>
</html>
