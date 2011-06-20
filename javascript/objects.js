/*
###################################################
##############   Global Values    #################
###################################################
*/

// Buttons flags
var p_count=new Array();
var c_count=new Array();
var Sp_count=new Array();
var Sc_count=new Array();
var Rp_count=new Array();
var Rc_count=new Array();

// Ajax Post request
var http_request = false;

// Teminal history content
var bash_content = '';
// Host current ping ip
var css_type = 'normal_';
// Caret position
var caret_pos = 0;

/*
###################################################
############## <CANVAS> Functions #################
###################################################
*/
/*
Draw Hosts and set coordinates
*/
function draw_host(ObjectCanvas,x,y) {
   var canvas = document.getElementById(ObjectCanvas);
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        
        // Drawing a trapeze
        ctx.fillStyle = "rgba(10,10,10,0.3)";// gray
        ctx.beginPath();
        ctx.moveTo(0+x,55+y);  
        ctx.lineTo(10+x,45+y);
        ctx.lineTo(70+x,45+y); 
        ctx.lineTo(80+x,55+y);  
        ctx.lineTo(0+x,55+y);  
        ctx.stroke();
        ctx.fill();
   
        ctx.strokeRect(25+x,5+y,30,30);
        ctx.fillRect (25+x, 5+y, 30, 30);//  fillRect(x,y,width,height)
      }
}

/*
Draw Terminal
*/
function draw_terminal(ObjectCanvas,w,h) {
   var canvas = document.getElementById(ObjectCanvas);
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        canvas.width = 640+w;
        canvas.height = 490+h;
        
        ctx.globalCompositeOperation = 'destination-over';
        ctx.fillStyle = "#43423d";
        ctx.fillRect (0, -20, 660+w, 75);
        ctx.fillStyle = "rgba(54,12,43,0.8)";// purple
        ctx.fillRect (0, 0, 660+w, 500+h);//  fillRect(x,y,width,height)
      }
}

/*
Draw Host power button
*/
function draw_circle(ObjectCanvas, w, h, cs, str) {
   var canvas = document.getElementById(ObjectCanvas);
   canvas.width = w;
   canvas.height = h;
   var x = 0;
   var y = 3;
   
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        
        ctx.beginPath();
        ctx.lineWidth=3.5;
        ctx.fillStyle = cs;
        ctx.strokeStyle  = cs;
        ctx.arc((w/2),(h/2)-13,16,-1.25,4.4,false);
        ctx.stroke();
        ctx.moveTo(w/2,(h/2)-16);
        ctx.lineTo(40,7);
        ctx.stroke();
        ctx.closePath();
        
        ctx.textAlign = "center";
        textBaseline = "bottom";
        ctx.fillText("power "+str, (w/2)-2, h-2);
        
        // Drawing a trapeze
        ctx.lineWidth=1.5;
        ctx.fillStyle = "rgba(10,10,10,0.3)";// gray
        ctx.strokeStyle = "rgba(0,0,0,0.8)";
        ctx.beginPath();
        ctx.moveTo(0+x,55+y);  
        ctx.lineTo(10+x,45+y);
        ctx.lineTo(70+x,45+y); 
        ctx.lineTo(80+x,55+y);  
        ctx.lineTo(0+x,55+y);  
        ctx.stroke();
        ctx.fill();
   
        ctx.strokeRect(20+x,1+y,40,40);
        ctx.fillRect (20+x, 1+y, 40, 40);//  fillRect(x,y,width,height)
      }
}

/*
Draw Host cable button
*/
function draw_rect(ObjectCanvas, w, h, cs, str) {
   var canvas = document.getElementById(ObjectCanvas);
   canvas.width = w;
   canvas.height = h;
   
   var black = "#000000";
   var yellow = "#FFCC11";
   var m;
   
      if (cs != "rgb(139,139,131)"){

          var black = cs;
          var yellow = cs;
        
      }
   
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        
        ctx.fillStyle = "rgb(105,105,105)";
        ctx.strokeStyle  = cs;
        ctx.fillRect(4,5,42,35);
        
        ctx.globalCompositeOperation = 'source-over';
        ctx.fillStyle = black;
        ctx.fillRect(8,9,34,20);
        
        ctx.beginPath();
        ctx.lineWidth=3;
        ctx.strokeStyle  = black;
        ctx.moveTo(12,30);
        ctx.lineTo(38,30);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.lineWidth=3;
        ctx.strokeStyle  = black;
        ctx.moveTo(16,32);
        ctx.lineTo(34,32);
        ctx.stroke();
        
        
        var c=-7;//x
        var d=-18;//y
        
        for (var n=0;n<7;n++){
            m=n*4;
            ctx.beginPath();
            ctx.lineWidth=2;
            ctx.strokeStyle  = yellow;
            ctx.moveTo(20+c+m,28+d);
            ctx.lineTo(20+c+m,32+d);
            ctx.stroke();
        }
        
        ctx.fillStyle = cs;
        ctx.strokeStyle  = cs;
        
        //Text
        ctx.textAlign = "center";
        textBaseline = "bottom";
        ctx.fillText(str, (w/2)-2, h-7);
      }
}


/*
Draw Switch power button
*/
function power_switch(ObjectCanvas, w, h, cs, str) {
   var canvas = document.getElementById(ObjectCanvas);
   canvas.width = w;
   canvas.height = h;
   var x = 0;
   var y = 5;
   var a = 3;
   var b = -3;
   
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        
        //power
        ctx.beginPath();
        ctx.lineWidth=3.5;
        ctx.fillStyle = cs;
        ctx.strokeStyle  = cs;
        ctx.arc((w/2)+a,(h/2)-21+b,16,-1.25,4.4,false);
        ctx.stroke();
        ctx.moveTo((w/2)+a,(h/2)-25+b);
        ctx.lineTo(35+a,5+b);
        ctx.stroke();
        ctx.closePath();
        
        // Text
        ctx.textAlign = "center";
        textBaseline = "bottom";
        ctx.fillText("power "+str, (w/2)-6, h-5);
        
        ctx.lineWidth=1.5;
        ctx.fillStyle = "rgba(10,10,10,0.3)";// gray
        ctx.strokeStyle = "rgba(0,0,0,0.8)";
        // Diamond
        ctx.beginPath();
        ctx.moveTo(4+x,49+y);  
        ctx.lineTo(16+x,34+y);
        ctx.lineTo(65+x,34+y); 
        ctx.lineTo(55+x,49+y);  
        ctx.lineTo(4+x,49+y);
        // 3d part
        ctx.lineTo(4+x,60+y);
        ctx.lineTo(55+x,60+y);
        ctx.lineTo(55+x,49+y);
        ctx.lineTo(56+x,59.3+y);
        ctx.lineTo(65.5+x,45+y);
        ctx.lineTo(65.5+x,34+y);
        ctx.stroke();
        ctx.fill();
      }
}

/*
Draw Switch cable button
*/
function cable_switch(ObjectCanvas, w, h, cs, str) {
   var canvas = document.getElementById(ObjectCanvas);
   canvas.width = w;
   canvas.height = h;
   var x = -5;
   var y = -6;
   var m;
   var black = "#000";
   
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        
        if (cs != "rgb(139,139,131)"){
            black = cs;
        }
        
        //Color Style
        ctx.fillStyle = cs;
        // Text
        ctx.textAlign = "center";
        textBaseline = "bottom";
        ctx.fillText(str, (w/2)-1, h-2);
        
        // Draw outside
        ctx.fillStyle = "rgb(139,139,131)";
        for (var n=0;n<5;n++){
            m=n*15;
            ctx.fillRect(5+x,6+y+m,20,13);
        }
        
        ctx.globalCompositeOperation = 'source-over';
        ctx.lineWidth=2;
        ctx.strokeStyle = black;
        ctx.fillStyle = black;
        
        // Draw inside
        for (var n=0;n<5;n++){
            m=n*15;
            ctx.fillRect(8+x,8+y+m,14,7);
            
            ctx.beginPath();
            ctx.moveTo(10+x,15+y+m);
            ctx.lineTo(20+x,15+y+m);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(12+x,16+y+m);
            ctx.lineTo(18+x,16+y+m);
            ctx.stroke();
            
        }
        
      }
}

/*
Draw Router power button
*/
function power_router(ObjectCanvas, w, h, cs, str) {
   var canvas = document.getElementById(ObjectCanvas);
   canvas.width = w;
   canvas.height = h;
   var x = 1;
   var y = 0;
   var a = 3;
   var b = -3;
   
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        
        //power
        ctx.beginPath();
        ctx.lineWidth=3.5;
        ctx.fillStyle = cs;
        ctx.strokeStyle  = cs;
        ctx.arc((w/2)+a,(h/2)-21+b,16,-1.25,4.4,false);
        ctx.globalCompositeOperation = 'destination-over';
        ctx.stroke();
        ctx.moveTo((w/2)+a,(h/2)-25+b);
        ctx.lineTo(35+a,5+b);
        ctx.stroke();
        ctx.closePath();
        
        // Text
        ctx.textAlign = "center";
        textBaseline = "bottom";
        ctx.fillText("power "+str, (w/2)-2, h-5);
        
        ctx.beginPath();
        ctx.lineWidth=1.5;
         ctx.fillStyle = "#c0c0c0";//Gray
        ctx.strokeStyle = "rgb(0,0,0)";
        
        // Ellipse
        ctx.save();
        ctx.scale(1, 0.5);
        ctx.beginPath();
        ctx.arc(37+x,85+y, 25, 0, Math.PI*2, false);
        ctx.stroke();
        ctx.fill();
        ctx.closePath();
        ctx.restore();
        
        ctx.globalCompositeOperation = 'destination-over';
        
        ctx.save();
        ctx.scale(1, 0.5);
        ctx.beginPath();
        
        ctx.arc(37+x,105+y, 25.6, 0, Math.PI*2, false);
        ctx.stroke();
        ctx.fill();
        ctx.closePath();
        ctx.restore();
        ctx.beginPath();
        ctx.lineWidth=1.5;
        ctx.lineTo(12+x,42+y);
        ctx.lineTo(12+x,54.5+y);
        ctx.stroke();
        ctx.beginPath();
        ctx.lineWidth=1.5;
        ctx.lineTo(62+x,42+y);
        ctx.lineTo(62+x,54.5+y);
        ctx.stroke();
        ctx.fill();
      }
}

/*
Draw Router cable button
*/
function cable_router(ObjectCanvas, w, h, cs, str) {
   var canvas = document.getElementById(ObjectCanvas);
   canvas.width = w;
   canvas.height = h;
   var x = -5;
   var y = -4;
   var m;
   var black = "#000";
   
      if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        
        if (cs != "rgb(139,139,131)"){
            black = cs;
        }
        
        //Color Style
        ctx.fillStyle = cs;
        // Text
        ctx.textAlign = "center";
        textBaseline = "bottom";
        ctx.fillText(str, (w/2)-3, h-5);
        
        // Draw outside
        ctx.fillStyle = "rgb(139,139,131)";
        for (var n=0;n<4;n++){
            m=n*15;
            ctx.fillRect(5+x,6+y+m,20,13);
        }
        
        ctx.globalCompositeOperation = 'source-over';
        ctx.lineWidth=2;
        ctx.strokeStyle = black;
        ctx.fillStyle = black;
        
        // Draw inside
        for (var n=0;n<4;n++){
            m=n*15;
            ctx.fillRect(8+x,8+y+m,14,7);
            
            ctx.beginPath();
            ctx.moveTo(10+x,15+y+m);
            ctx.lineTo(20+x,15+y+m);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(12+x,16+y+m);
            ctx.lineTo(18+x,16+y+m);
            ctx.stroke();
            
        }
      }
}

/*
###################################################
##############  Control Functions #################
###################################################
*/
/*
Catch the caret position of ctrl ans store in caret_pos
*/
function doGetCaretPosition (ctrl) {
	// IE Support
	if (document.selection) {
	ctrl.focus ();
		var Sel = document.selection.createRange ();
		Sel.moveStart ('character', -ctrl.value.length);
		caret_pos = Sel.text.length;
	}
	// Firefox support
	else if (ctrl.selectionStart || ctrl.selectionStart == '0')
		caret_pos = bash_content.length;
}

/*
Set caret position
*/
function setCaretPosition(ctrl){
    // get caret position
    doGetCaretPosition (ctrl);

	if(ctrl.setSelectionRange)
	{
		ctrl.focus();
		ctrl.setSelectionRange(caret_pos,caret_pos);
	}
	else if (ctrl.createTextRange) {
		var range = ctrl.createTextRange();
		range.collapse(true);
		range.moveEnd('character', caret_pos);
		range.moveStart('character', caret_pos);
		range.select();
	}
}


/*
Find equipment
*/
function find_equipment(eq) {
    // Find host
    if (eq[0] == 'H'){
        for (var n=0;n<12;n++){
            if (eq == 'H'+n){
                return n;
            }
        }
    }
    else if (eq[0] == 'S'){
        for (var n=0;n<3;n++){
            if (eq == 'S'+n){
                return n;
            }
        }
    }
    else if (eq[0] == 'R'){
        for (var n=0;n<3;n++){
            if (eq == 'R'+n){
                return n;
            }
        }
    }
}

/*
Control on/off power button
*/
function change_power(eq){
   var n = find_equipment(eq);
   // Hosts
   if (eq[0] == 'H'){
       if (p_count[n] == 0){
           draw_circle("power"+eq[0]+n,80,75,"rgb(0,191,255)","on");
           p_count[n] = 1;
           // Send to server get_button(eq,power,cable)
           get_button(eq,p_count[n],c_count[n]);
       }
       else{
           draw_circle("power"+eq[0]+n,80,75,"rgb(105,105,105)","off");
           p_count[n] = 0;
           // Send to server get_button(eq,power,cable)
           get_button(eq,p_count[n],c_count[n]);
       }
   }
   // Switchs
   else if (eq[0] == 'S'){
       if (Sp_count[n] == 0){
           power_switch("powerS"+n,70,87,"rgb(0,191,255)","on");
           Sp_count[n] = 1;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Sp_count[n],Sc_count[n]);
       }
       else{
           power_switch("powerS"+n,70,87,"rgb(105,105,105)","off");
           Sp_count[n] = 0;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Sp_count[n],Sc_count[n]);
       }
   }
   // Routers
   else if (eq[0] == 'R'){
       if (Rp_count[n] == 0){
           power_router("powerR"+n,70,87,"rgb(0,191,255)","on");
           Rp_count[n] = 1;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Rp_count[n],Rc_count[n]);
       }
       else{
           power_router("powerR"+n,70,87,"rgb(105,105,105)","off");
           Rp_count[n] = 0;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Rp_count[n],Rc_count[n]);
       }
   }
}

/*
Control on/off cable button
*/
function change_cable(eq){
   var n = find_equipment(eq);
   // Hosts
   if (eq[0] == 'H'){
       if (c_count[n] == 0){
           draw_rect("cable"+eq[0]+n,50,65,"rgb(0,200,0)","plugged");
           c_count[n] = 1;
           // Send to server get_button(eq,power,cable)
           get_button(eq,p_count[n],c_count[n]);
       }
       else{
           draw_rect("cable"+eq[0]+n,50,65,"rgb(139,139,131)","off-line");
           c_count[n] = 0;
           // Send to server get_button(eq,power,cable)
           get_button(eq,p_count[n],c_count[n]);
       }
   }
   // Switchs
   else if (eq[0] == 'S'){
       if (Sc_count[n] == 0){
           cable_switch("cableS"+n,20,87,"rgb(0,200,0)","on");
           Sc_count[n] = 1;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Sp_count[n],Sc_count[n]);
       }
       else{
           cable_switch("cableS"+n,20,87,"rgb(139,139,131)","off");
           Sc_count[n] = 0;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Sp_count[n],Sc_count[n]);
       }
   }
   // Routers
   else if (eq[0] == 'R'){
       if (Rc_count[n] == 0){
           cable_router("cableR"+n,20,87,"rgb(0,200,0)","on");
           Rc_count[n] = 1;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Rp_count[n],Rc_count[n]);
       }
       else{
           cable_router("cableR"+n,20,87,"rgb(105,105,105)","off");
           Rc_count[n] = 0;
           // Send to server get_button(eq,power,cable)
           get_button(eq,Rp_count[n],Rc_count[n]);
       }
   }
}

/*
Draw canvas objects
*/
function draw() {

   // Hosts
   for (var n=0;n<12;n++){
       draw_circle("powerH"+n,80,75,"rgb(105,105,105)","off");
       draw_rect("cableH"+n,50,65,"rgb(139,139,131)","off-line");
       c_count[n] = 0;
       p_count[n] = 0;
   }
   // Switchs
   for (var n=0;n<3;n++){
       power_switch("powerS"+n,70,87,"rgb(105,105,105)","off");
       cable_switch("cableS"+n,20,87,"rgb(139,139,131)","off");
       Sc_count[n] = 0;
       Sp_count[n] = 0;
   }
   // Routers
   for (var n=0;n<3;n++){
       power_router("powerR"+n,70,87,"rgb(105,105,105)","off");
       cable_router("cableR"+n,20,87,"rgb(139,139,131)","off");
       Rc_count[n] = 0;
       Rp_count[n] = 0;
   }
}

/*
###################################################
####### AJAX and comunication Functions ###########
###################################################
*/
/*
Information about how to play
*/ 
function howToPlay(swt) {
    
    var howtoHTML;
    
    if (swt == '1'){
        
        // HTML How to play
        howtoHTML='<div id="howto"><table><tr><tr><td><b>How to play</b></td><td></td></tr></tr><tr id="content"><td width="320px">About the network enviroment:<br><br>There are three networks :<br>201.10.0.0<br><dd>Router01<br></dd><dd>Switch01<br></dd><dd>Host01~04</dd><br><br>200.171.0.0<br><dd>Router02<br></dd><dd>Switch02<br></dd><dd>Host05~08</dd><br><br>192.168.0.0<br><dd>Router03<br></dd><dd>Switch03<br></dd><dd>Host09~12</dd><br><br>Routers:<br>Router01 can communicate with Router02;<br>Router02 can communicate with Router01 and 03;<br>and Router03 can communicate with Router02.<br><br>Switchs:<br>The Switchs make the communication<br> between the Router and the Hosts.</td><td width="320px">Start to play:<br><br>To start to play you need to turn on a host (click on host you want), connect cables and open the terminal (click on the Terminal button).<br><br>To know which commands you can use in the terminal type help (@169.254.0.0:~$ <b>help</b>) and press enter to see the command list.<br><br>Use the command <b>ping <i>IP</i></b> to test if there is communication between two hosts.<br><br>Command list:<br><br><b>help</b> get (this) commands list<br><b>ping [ip address]</b>  get ping<br><b>ifconfig</b>  get host information<br><b>ifconfig [ip address]</b>  set IP<br><b>netmask [mask address]</b>  set mask<br><b>ifconfig [ip address] netmask [mask address]</b> set IP and Mask<br><b>route</b> get host routes<br><b>clear</b>  clean bash<br><b>bash --version</b>  see bash version<br><b>date</b>  get today date<br><button style="float: right;" onclick="javascript:howToPlay(0);" type="button">Close</button></td></tr></div>';
    }
    else if (swt == '0'){
         howtoHTML='';
    }
   document.getElementById('tAjax').innerHTML = howtoHTML;

}

/*
Get elements values from the form
Define url destination
*/    
function changeCSS(n,css) {

    var cmd_split;
    var sub_cmd_split;
    var ip;
    var re; 
    
    //Change CSS
    css_type = css;
    
    //Find IP
    cmd_split = bash_content.split('\n');
    cmd_split = cmd_split[(cmd_split.length)-1]
    
    re = new RegExp('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}');
    ip = re.exec(cmd_split)
    
    //Rebuild terminal
    makeTerminal(n,bash_content,ip,css_type);

}

/*
Get elements values from the form
Define url destination
*/    
function get(obj,n) {

    var cmd_split;
    var sub_cmd_split;
    var poststr;
    var re;
    var ip;
    
    // Store all content in Global bash_content
    bash_content = document.getElementById('textarea').value;
            
    //Find command
    cmd_split = bash_content.split('\n');
    cmd = cmd_split[(cmd_split.length)-1]
    
    var s = cmd.indexOf('$')+1;
    if (cmd[s] != ' '){cmd = cmd.substr(0,s)+' '+cmd.substr(s);}
    
    cmd_split = cmd.split('$ ');
    
    re = new RegExp('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}');
    ip = re.exec(cmd)
    
    if(typeof(cmd_split[1])!='undefined'){
        sub_cmd_split = cmd_split[1].split(' ');
        
    }
    
    /* #####################################
        Bash commands JavaScript dictionary
       #####################################
    */
    
    // Disconnected
    if (p_count[n] == 0){
        alert('Turn on computer!\nコンピュータの電源を入れてください！');
    }
    
    // undefined - first time
    else if(typeof(cmd_split[1])=='undefined'){ 
        cmd_split[1]=' ';
        poststr = 'host=' + encodeURI( n )+'&textarea=' + encodeURI( cmd_split[1] );
        makePOSTRequest('/ping', poststr);
    }
    
    // exit
    else if(cmd_split[1]=='exit'){
        //Clean values
        bash_content = '';
        document.getElementById('tAjax').innerHTML = '';
    }
    
    else if (sub_cmd_split[0]=='ping' &&  (sub_cmd_split[1]=='-help' || sub_cmd_split[1]=='-h' || sub_cmd_split[1]=='--help') && (sub_cmd_split.length == 2)){
        //alert('help');
        
        bash_content+='\nUsage: ping [ IP destination ]';
        bash_content+='\n@'+ip+':~$ ';
        makeTerminal(n,bash_content,ip,css_type);
    }
    
    else if (sub_cmd_split[0]=='ifconfig' &&  (sub_cmd_split[1]=='-help' || sub_cmd_split[1]=='-h'|| sub_cmd_split[1]=='--help') && (sub_cmd_split.length == 2)){
        //alert('help');
        
        bash_content+='\nUsage:\n  ifconfig [<ip address>] [netmask <address>]';
        bash_content+='\n  ifconfig [<ip address>]';
        bash_content+='\n@'+ip+':~$ ';
        makeTerminal(n,bash_content,ip,css_type);
    }
    
    // ping - first line
    else if((sub_cmd_split[0]=='ping') && (re.exec(sub_cmd_split[1])!=null)){
    
        var ip = re.exec(cmd_split[0]);
        
        bash_content += '\nPING '+sub_cmd_split[1]+' ('+sub_cmd_split[1]+') 56(84) bytes of data.';
        
        // send n, bash, IP
        makeTerminal(n,bash_content,ip,css_type);
      
        poststr = 'host=' + encodeURI( n )+'&textarea=' + encodeURI( cmd_split[1] );
        makePOSTRequest('/ping', poststr);
    }
    else{
        //alert("cmd_split:"+cmd_split[1]);
        poststr = 'host=' + encodeURI( n )+'&textarea=' + encodeURI( cmd_split[1] );
        makePOSTRequest('/ping', poststr);
    }
}

function makeTerminal(n, b, ip, css) {
    
    var w = 0;
    var h = 0;
    var len;
    var max_button = '<button onclick="javascript:changeCSS('+n+',\'maximize_\')" type="button">[&nbsp;&nbsp;&nbsp;]</button>';
    var min_button = '<button onclick="javascript:changeCSS('+n+',\'minimize_\')" type="button">-</button>';
    
    if (css =='maximize_'){
        max_button = '<button onclick="javascript:changeCSS('+n+',\'normal_\')" type="button">[&nbsp;]</button>';
        w=400;
        h=150;
    }
    else if (css =='minimize_'){
        min_button = '<button onclick="javascript:changeCSS('+n+',\'normal_\')" type="button">_</button>';
        w=-350;
        h=-450;
    }
    else{
        css =='normal_'
        w=0;
        h=0;
    }
    
    var num=parseInt(n);
    num+=1;
        
    // HTML Terminal 
    var terminalHTML = '<div id='+css+'><canvas id="cmd" width=640 height=490></canvas><div id="'+css+'terminal_title">host '+num+'@'+ip+'</div><form><div id="'+css+'buttons">'+min_button+max_button+'<button type="button" onclick="javascript:textarea.value=\'@169.254.0.0:~$ exit\';get(this.parentNode,'+n+');" >x</button></div><textarea id="textarea" class="'+css+'textarea" onMouseOut="javascript:doGetCaretPosition(textarea);" onclick="javascript:setCaretPosition(textarea);"  onKeyDown="javascript:if(event.keyCode == \'13\'){return false;}else if(event.keyCode == \'9\'){return false;}" onKeyUp="javascript:if(event.keyCode == \'13\'){get(this.parentNode,'+n+');return false;}else if(event.keyCode == \'9\'){return false;}">'+b+'</textarea></form></div>';
    
    // Writting in the page ajax area
    document.getElementById('tAjax').innerHTML = terminalHTML;
    
    //drawing <canvas>
    draw_terminal("cmd",w,h);
    
    //Chrome
    //overflow:scroll;
    //scrollTop:scroll;
    
    //alert(document.getElementById('textarea').scrollHeight);
    
    
    document.getElementById('textarea').scrollTop=document.getElementById('textarea').scrollHeight;
    document.body.scrollTop = document.getElementById('textarea').scrollHeight;
    document.getElementById('textarea').focus();
    
    document.body.scrollTop = document.getElementById('textarea').scrollHeight;
      
    alert('Textarea:'+document.getElementById('textarea').scrollTop+' body:'+document.body.scrollTop+' Get:'+document.getElementById('textarea').getScrollTop() );
    alert(document.body.scrollTop);
}

/*
Post Ajax sends function
*/ 
function makePOSTRequest(url, parameters) {
    http_request = false;
    if (window.XMLHttpRequest) { // Mozilla, Safari,...
        http_request = new XMLHttpRequest();
        if (http_request.overrideMimeType) {
     	    // set type accordingly to anticipated content type
            //http_request.overrideMimeType('text/xml');
            http_request.overrideMimeType('text/html');
        }
    } 
    else if (window.ActiveXObject) { // IE
        try {
            http_request = new ActiveXObject("Msxml2.XMLHTTP");
        } 
        catch (e) {
            try {
                http_request = new ActiveXObject("Microsoft.XMLHTTP");
            } 
            catch (e) {}
        }
    }
    if (!http_request) {
         alert('Cannot create XMLHTTP instance');
         return false;
    }
    http_request.onreadystatechange = alertContents;
    http_request.open('POST', url, true);
    http_request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    /*
    Chrome unsafe names problems
    http_request.setRequestHeader("Content-length", parameters.length);
    http_request.setRequestHeader("Connection", "close");
    */
    http_request.send(parameters);
}

function dictionary_cmd(result){

    var param;
    var sub_param;
    
    if(typeof(result)!='undefined'){
        param = result.split('|:|');
    }
    else{
        return false;
    }
    if(typeof(param[1])!='undefined'){ 
        sub_param = param[1].split(' ');   
    }
    else{
        return false;
    }
    
    // clear
    if (param[1] == 'clear'){
        //alert('clear');          
                        
        bash_content = '@'+param[2]+':~$ ';
        // send n, bash, terminal_title
        makeTerminal(param[0],bash_content,param[2],css_type);
        return true;
              
     }
     
     // bash --version
     else if (sub_param[0] == 'bash' && sub_param[1] == '--version'){
        //alert('bash --version');
        
        bash_content += '\nMoreno bash, version 1.5(1)-release (x86_64-pc-linux-gnu)\nGaiaX (c)';
        bash_content += '\n@'+param[2]+':~$ ';
        // send n, bash, terminal_title
        makeTerminal(param[0],bash_content,param[2],css_type);
        return true;
     }
     
     // help
     else if (param[1] == 'help'){
        //alert('help');
        
        // HTML help
        bash_content += '\nCOMMANDs:\nhelp ........................................ get commands list\nping [ip address] ........................... get ping\nifconfig .................................... get host information\nifconfig [ip address] ....................... set IP\nnetmask [mask address] ...................... set mask\nifconfig [ip address] netmask [mask address]  set IP and Mask\nroute ....................................... host routes\nclear ....................................... clean bash\nbash --version .............................. bash version\ndate ........................................ today date\nexit......................................... quit';
        bash_content += '\n@'+param[2]+':~$ ';
        // send n, bash, terminal_title
        makeTerminal(param[0],bash_content,param[2],css_type);
        return true;
     }
     
     //ping looping
     else if ((sub_param[0] == "\n64") && (param[1].length < 90)){
                
        bash_content += param[1];
        makeTerminal(param[0],bash_content,param[2],css_type);
        
        // Send ping ip 0.0.0.0 second and more times
        // Important IP(0.0.0.0) to looping test          
        var poststr = 'host=' + encodeURI(param[0])+'&textarea=' + encodeURI('ping 0.0.0.0');
        makePOSTRequest('/ping', poststr);
        return true;                
     }
     else{
        return false;
     }
}

/*
Post Ajax receives function
*/    
function alertContents() {
    if (http_request.readyState == 4) {
        if (http_request.status == 200) {
                        
            // Server response
            result = http_request.responseText;
            
            if(result != 0){                
                if (!dictionary_cmd(result)){                    
                    var param = result.split("|:|");
                    bash_content += param[1]+"\n@"+param[2]+":~$ ";
                    makeTerminal(param[0],bash_content,param[2],css_type);
                } 
            }         
         }
         else {
            alert('There was a problem with the request.');
         }
   }
}

function get_button(eq,p,c) {
    
    var poststr = "power=" + encodeURI( eq )+"&cable=" + encodeURI( eq )+"&pctrl=" + encodeURI( p )+"&cctrl=" + encodeURI( c );
    makePOSTRequest('/on', poststr);
}
