window.Modernizr=function(at,av,M){function O(a){R.cssText=a}function S(a,b){return O(ad.join(a+";")+(b||""))}function W(a,b){return typeof a===b}function aa(a,b){return !!~(""+a).indexOf(b)}function ae(a,b){for(var c in a){var d=a[c];if(!aa(d,"-")&&R[d]!==M){return b=="pfx"?d:!0}}return !1}function L(a,b,c){for(var d in a){var e=b[a[d]];if(e!==M){return c===!1?a[d]:W(e,"function")?e.bind(c||b):e}}return !1}function P(a,b,c){var d=a.charAt(0).toUpperCase()+a.slice(1),e=(a+" "+ah.join(d+" ")+d).split(" ");return W(b,"string")||W(b,"undefined")?ae(e,b):(e=(a+" "+ai.join(d+" ")+d).split(" "),L(e,b,c))}function T(){U.input=function(a){for(var b=0,c=a.length;b<c;b++){am[a[b]]=a[b] in V}return am.list&&(am.list=!!av.createElement("datalist")&&!!at.HTMLDataListElement),am}("autocomplete autofocus list placeholder max min multiple pattern required step".split(" ")),U.inputtypes=function(a){for(var b=0,c,d,e,f=a.length;b<f;b++){V.setAttribute("type",d=a[b]),c=V.type!=="text",c&&(V.value=Z,V.style.cssText="position:absolute;visibility:hidden;",/^range$/.test(d)&&V.style.WebkitAppearance!==M?(ac.appendChild(V),e=av.defaultView,c=e.getComputedStyle&&e.getComputedStyle(V,null).WebkitAppearance!=="textfield"&&V.offsetHeight!==0,ac.removeChild(V)):/^(search|tel)$/.test(d)||(/^(url|email)$/.test(d)?c=V.checkValidity&&V.checkValidity()===!1:c=V.value!=Z)),al[a[b]]=!!c}return al}("search tel url email datetime date month week time datetime-local number range color".split(" "))}var Q="2.8.3",U={},Y=!0,ac=av.documentElement,ag="modernizr",N=av.createElement(ag),R=N.style,V=av.createElement("input"),Z=":)",ab={}.toString,ad=" -webkit- -moz- -o- -ms- ".split(" "),af="Webkit Moz O ms",ah=af.split(" "),ai=af.toLowerCase().split(" "),aj={svg:"http://www.w3.org/2000/svg"},ak={},al={},am={},an=[],ao=an.slice,ap,aq=function(a,b,c,d){var e,f,g,h,i=av.createElement("div"),j=av.body,k=j||av.createElement("body");if(parseInt(c,10)){while(c--){g=av.createElement("div"),g.id=d?d[c]:ag+(c+1),i.appendChild(g)}}return e=["&#173;",'<style id="s',ag,'">',a,"</style>"].join(""),i.id=ag,(j?i:k).innerHTML+=e,k.appendChild(i),j||(k.style.background="",k.style.overflow="hidden",h=ac.style.overflow,ac.style.overflow="hidden",ac.appendChild(k)),f=b(i,a),j?i.parentNode.removeChild(i):(k.parentNode.removeChild(k),ac.style.overflow=h),!!f},ar=function(){function b(c,d){d=d||av.createElement(a[c]||"div"),c="on"+c;var e=c in d;return e||(d.setAttribute||(d=av.createElement("div")),d.setAttribute&&d.removeAttribute&&(d.setAttribute(c,""),e=W(d[c],"function"),W(d[c],"undefined")||(d[c]=M),d.removeAttribute(c))),d=null,e}var a={select:"input",change:"input",submit:"form",reset:"form",error:"img",load:"img",abort:"img"};return b}(),au={}.hasOwnProperty,aw;!W(au,"undefined")&&!W(au.call,"undefined")?aw=function(a,b){return au.call(a,b)}:aw=function(a,b){return b in a&&W(a.constructor.prototype[b],"undefined")},Function.prototype.bind||(Function.prototype.bind=function(a){var b=this;if(typeof b!="function"){throw new TypeError}var c=ao.call(arguments,1),d=function(){if(this instanceof d){var e=function(){};e.prototype=b.prototype;var f=new e,g=b.apply(f,c.concat(ao.call(arguments)));return Object(g)===g?g:f}return b.apply(a,c.concat(ao.call(arguments)))};return d}),ak.flexbox=function(){return P("flexWrap")},ak.canvas=function(){var a=av.createElement("canvas");return !!a.getContext&&!!a.getContext("2d")},ak.canvastext=function(){return !!U.canvas&&!!W(av.createElement("canvas").getContext("2d").fillText,"function")},ak.webgl=function(){return !!at.WebGLRenderingContext},ak.touch=function(){var a;return"ontouchstart" in at||at.DocumentTouch&&av instanceof DocumentTouch?a=!0:aq(["@media (",ad.join("touch-enabled),("),ag,")","{#modernizr{top:9px;position:absolute}}"].join(""),function(b){a=b.offsetTop===9}),a},ak.geolocation=function(){return"geolocation" in navigator},ak.postmessage=function(){return !!at.postMessage},ak.websqldatabase=function(){return !!at.openDatabase},ak.indexedDB=function(){return !!P("indexedDB",at)},ak.hashchange=function(){return ar("hashchange",at)&&(av.documentMode===M||av.documentMode>7)},ak.history=function(){return !!at.history&&!!history.pushState},ak.draganddrop=function(){var a=av.createElement("div");return"draggable" in a||"ondragstart" in a&&"ondrop" in a},ak.websockets=function(){return"WebSocket" in at||"MozWebSocket" in at},ak.rgba=function(){return O("background-color:rgba(150,255,150,.5)"),aa(R.backgroundColor,"rgba")},ak.hsla=function(){return O("background-color:hsla(120,40%,100%,.5)"),aa(R.backgroundColor,"rgba")||aa(R.backgroundColor,"hsla")},ak.multiplebgs=function(){return O("background:url(https://),url(https://),red url(https://)"),/(url\s*\(.*?){3}/.test(R.background)},ak.backgroundsize=function(){return P("backgroundSize")},ak.borderimage=function(){return P("borderImage")},ak.borderradius=function(){return P("borderRadius")},ak.boxshadow=function(){return P("boxShadow")},ak.textshadow=function(){return av.createElement("div").style.textShadow===""},ak.opacity=function(){return S("opacity:.55"),/^0.55$/.test(R.opacity)},ak.cssanimations=function(){return P("animationName")},ak.csscolumns=function(){return P("columnCount")},ak.cssgradients=function(){var a="background-image:",b="gradient(linear,left top,right bottom,from(#9f9),to(white));",c="linear-gradient(left top,#9f9, white);";return O((a+"-webkit- ".split(" ").join(b+a)+ad.join(c+a)).slice(0,-a.length)),aa(R.backgroundImage,"gradient")},ak.cssreflections=function(){return P("boxReflect")},ak.csstransforms=function(){return !!P("transform")},ak.csstransforms3d=function(){var a=!!P("perspective");return a&&"webkitPerspective" in ac.style&&aq("@media (transform-3d),(-webkit-transform-3d){#modernizr{left:9px;position:absolute;height:3px;}}",function(b,c){a=b.offsetLeft===9&&b.offsetHeight===3}),a},ak.csstransitions=function(){return P("transition")},ak.fontface=function(){var a;return aq('@font-face {font-family:"font";src:url("https://")}',function(b,c){var d=av.getElementById("smodernizr"),e=d.sheet||d.styleSheet,f=e?e.cssRules&&e.cssRules[0]?e.cssRules[0].cssText:e.cssText||"":"";a=/src/i.test(f)&&f.indexOf(c.split(" ")[0])===0}),a},ak.generatedcontent=function(){var a;return aq(["#",ag,"{font:0/0 a}#",ag,':after{content:"',Z,'";visibility:hidden;font:3px/1 a}'].join(""),function(b){a=b.offsetHeight>=3}),a},ak.video=function(){var a=av.createElement("video"),b=!1;try{if(b=!!a.canPlayType){b=new Boolean(b),b.ogg=a.canPlayType('video/ogg; codecs="theora"').replace(/^no$/,""),b.h264=a.canPlayType('video/mp4; codecs="avc1.42E01E"').replace(/^no$/,""),b.webm=a.canPlayType('video/webm; codecs="vp8, vorbis"').replace(/^no$/,"")}}catch(c){}return b},ak.audio=function(){var a=av.createElement("audio"),b=!1;try{if(b=!!a.canPlayType){b=new Boolean(b),b.ogg=a.canPlayType('audio/ogg; codecs="vorbis"').replace(/^no$/,""),b.mp3=a.canPlayType("audio/mpeg;").replace(/^no$/,""),b.wav=a.canPlayType('audio/wav; codecs="1"').replace(/^no$/,""),b.m4a=(a.canPlayType("audio/x-m4a;")||a.canPlayType("audio/aac;")).replace(/^no$/,"")}}catch(c){}return b},ak.localstorage=function(){try{return localStorage.setItem(ag,ag),localStorage.removeItem(ag),!0}catch(a){return !1}},ak.sessionstorage=function(){try{return sessionStorage.setItem(ag,ag),sessionStorage.removeItem(ag),!0}catch(a){return !1}},ak.webworkers=function(){return !!at.Worker},ak.applicationcache=function(){return !!at.applicationCache},ak.svg=function(){return !!av.createElementNS&&!!av.createElementNS(aj.svg,"svg").createSVGRect},ak.inlinesvg=function(){var a=av.createElement("div");return a.innerHTML="<svg/>",(a.firstChild&&a.firstChild.namespaceURI)==aj.svg},ak.smil=function(){return !!av.createElementNS&&/SVGAnimate/.test(ab.call(av.createElementNS(aj.svg,"animate")))},ak.svgclippaths=function(){return !!av.createElementNS&&/SVGClipPath/.test(ab.call(av.createElementNS(aj.svg,"clipPath")))};for(var X in ak){aw(ak,X)&&(ap=X.toLowerCase(),U[ap]=ak[X](),an.push((U[ap]?"":"no-")+ap))}return U.input||T(),U.addTest=function(a,b){if(typeof a=="object"){for(var c in a){aw(a,c)&&U.addTest(c,a[c])}}else{a=a.toLowerCase();if(U[a]!==M){return U}b=typeof b=="function"?b():b,typeof Y!="undefined"&&Y&&(ac.className+=" "+(b?"":"no-")+a),U[a]=b}return U},O(""),N=V=null,function(q,r){function j(t,u){var v=t.createElement("p"),w=t.getElementsByTagName("head")[0]||t.documentElement;return v.innerHTML="x<style>"+u+"</style>",w.insertBefore(v.lastChild,w.firstChild)}function k(){var t=f.elements;return typeof t=="string"?t.split(" "):t}function l(t){var u=h[t[e]];return u||(u={},g++,t[e]=g,h[g]=u),u}function m(t,u,v){u||(u=r);if(i){return u.createElement(t)}v||(v=l(u));var w;return v.cache[t]?w=v.cache[t].cloneNode():c.test(t)?w=(v.cache[t]=v.createElem(t)).cloneNode():w=v.createElem(t),w.canHaveChildren&&!b.test(t)&&!w.tagUrn?v.frag.appendChild(w):w}function n(t,u){t||(t=r);if(i){return t.createDocumentFragment()}u=u||l(t);var v=u.frag.cloneNode(),w=0,x=k(),y=x.length;for(;w<y;w++){v.createElement(x[w])}return v}function o(t,u){u.cache||(u.cache={},u.createElem=t.createElement,u.createFrag=t.createDocumentFragment,u.frag=u.createFrag()),t.createElement=function(v){return f.shivMethods?m(v,t,u):u.createElem(v)},t.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+k().join().replace(/[\w\-]+/g,function(v){return u.createElem(v),u.frag.createElement(v),'c("'+v+'")'})+");return n}")(f,u.frag)}function p(t){t||(t=r);var u=l(t);return f.shivCSS&&!d&&!u.hasCSS&&(u.hasCSS=!!j(t,"article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}mark{background:#FF0;color:#000}template{display:none}")),i||o(t,u),t}var s="3.7.0",a=q.html5||{},b=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,c=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,d,e="_html5shiv",g=0,h={},i;(function(){try{var t=r.createElement("a");t.innerHTML="<xyz></xyz>",d="hidden" in t,i=t.childNodes.length==1||function(){r.createElement("a");var v=r.createDocumentFragment();return typeof v.cloneNode=="undefined"||typeof v.createDocumentFragment=="undefined"||typeof v.createElement=="undefined"}()}catch(u){d=!0,i=!0}})();var f={elements:a.elements||"abbr article aside audio bdi canvas data datalist details dialog figcaption figure footer header hgroup main mark meter nav output progress section summary template time video",version:s,shivCSS:a.shivCSS!==!1,supportsUnknownElements:i,shivMethods:a.shivMethods!==!1,type:"default",shivDocument:p,createElement:m,createDocumentFragment:n};q.html5=f,p(r)}(this,av),U._version=Q,U._prefixes=ad,U._domPrefixes=ai,U._cssomPrefixes=ah,U.hasEvent=ar,U.testProp=function(a){return ae([a])},U.testAllProps=P,U.testStyles=aq,U.prefixed=function(a,b,c){return b?P(a,b,c):P(a,"pfx")},ac.className=ac.className.replace(/(^|\s)no-js(\s|$)/,"$1$2")+(Y?" js "+an.join(" "):""),U}(this,this.document),function(I,K,M){function N(a){return"[object Function]"==Y.call(a)}function O(a){return"string"==typeof a}function P(){}function Q(a){return !a||"loaded"==a||"complete"==a||"uninitialized"==a}function R(){var a=Z.shift();aa=1,a?a.t?W(function(){("c"==a.t?L.injectCss:L.injectJs)(a.s,0,a.a,a.x,a.e,1)},0):(a(),R()):aa=0}function S(a,b,c,d,e,f,g){function h(m){if(!j&&Q(i.readyState)&&(l.r=j=1,!aa&&R(),i.onload=i.onreadystatechange=null,m)){"img"!=a&&W(function(){ad.removeChild(i)},50);for(var n in G[b]){G[b].hasOwnProperty(n)&&G[b][n].onload()}}}var g=g||L.errorTimeout,i=K.createElement(a),j=0,k=0,l={t:c,s:b,e:e,a:f,x:g};1===G[b]&&(k=1,G[b]=[]),"object"==a?i.data=b:(i.src=b,i.type=a),i.width=i.height="0",i.onerror=i.onload=i.onreadystatechange=function(){h.call(this,k)},Z.splice(d,0,l),"img"!=a&&(k||2===G[b]?(ad.insertBefore(i,ac?null:X),W(h,g)):G[b].push(i))}function T(a,b,c,d,e){return aa=0,b=b||"j",O(a)?S("c"==b?F:D,a,b,this.i++,c,d,e):(Z.splice(this.i++,0,a),1==Z.length&&R()),this}function U(){var a=L;return a.loader={load:T,i:0},a}var V=K.documentElement,W=I.setTimeout,X=K.getElementsByTagName("script")[0],Y={}.toString,Z=[],aa=0,ab="MozAppearance" in V.style,ac=ab&&!!K.createRange().compareNode,ad=ac?V:X.parentNode,V=I.opera&&"[object Opera]"==Y.call(I.opera),V=!!K.attachEvent&&!V,D=ab?"object":V?"script":"img",F=V?"script":D,C=Array.isArray||function(a){return"[object Array]"==Y.call(a)},E=[],G={},H={timeout:function(a,b){return b.length&&(a.timeout=b[0]),a}},J,L;L=function(a){function b(h){var h=h.split("!"),i=E.length,j=h.pop(),k=h.length,j={url:j,origUrl:j,prefixes:h},l,m,n;for(m=0;m<k;m++){n=h[m].split("="),(l=H[n.shift()])&&(j=l(j,n))}for(m=0;m<i;m++){j=E[m](j)}return j}function c(h,i,j,k,l){var m=b(h),n=m.autoCallback;m.url.split(".").pop().split("?").shift(),m.bypass||(i&&(i=N(i)?i:i[h]||i[k]||i[h.split("/").pop().split("?")[0]]),m.instead?m.instead(h,i,j,k,l):(G[m.url]?m.noexec=!0:G[m.url]=1,j.load(m.url,m.forceCSS||!m.forceJS&&"css"==m.url.split(".").pop().split("?").shift()?"c":M,m.noexec,m.attrs,m.timeout),(N(i)||N(n))&&j.load(function(){U(),i&&i(m.origUrl,l,k),n&&n(m.origUrl,l,k),G[m.url]=2})))}function d(h,i){function j(r,s){if(r){if(O(r)){s||(m=function(){var t=[].slice.call(arguments);n.apply(this,t),o()}),c(r,m,i,0,k)}else{if(Object(r)===r){for(q in p=function(){var t=0,u;for(u in r){r.hasOwnProperty(u)&&t++}return t}(),r){r.hasOwnProperty(q)&&(!s&&!--p&&(N(m)?m=function(){var t=[].slice.call(arguments);n.apply(this,t),o()}:m[q]=function(t){return function(){var u=[].slice.call(arguments);t&&t.apply(this,u),o()}}(n[q])),c(r[q],m,i,q,k))}}}}else{!s&&o()}}var k=!!h.test,l=h.load||h.both,m=h.callback||P,n=m,o=h.complete||P,p,q;j(k?h.yep:h.nope,!!l),l&&j(l)}var e,f,g=this.yepnope.loader;if(O(a)){c(a,0,g,0)}else{if(C(a)){for(e=0;e<a.length;e++){f=a[e],O(f)?c(f,0,g,0):C(f)?L(f):Object(f)===f&&d(f,g)}}else{Object(a)===a&&d(a,g)}}},L.addPrefix=function(a,b){H[a]=b},L.addFilter=function(a){E.push(a)},L.errorTimeout=10000,null==K.readyState&&K.addEventListener&&(K.readyState="loading",K.addEventListener("DOMContentLoaded",J=function(){K.removeEventListener("DOMContentLoaded",J,0),K.readyState="complete"},0)),I.yepnope=U(),I.yepnope.executeStack=R,I.yepnope.injectJs=function(a,b,c,d,e,f){var g=K.createElement("script"),h,i,d=d||L.errorTimeout;g.src=a;for(i in c){g.setAttribute(i,c[i])}b=f?R:b||P,g.onreadystatechange=g.onload=function(){!h&&Q(g.readyState)&&(h=1,b(),g.onload=g.onreadystatechange=null)},W(function(){h||(h=1,b(1))},d),e?g.onload():X.parentNode.insertBefore(g,X)},I.yepnope.injectCss=function(a,b,c,d,e,f){var d=K.createElement("link"),g,b=f?R:b||P;d.href=a,d.rel="stylesheet",d.type="text/css";for(g in c){d.setAttribute(g,c[g])}e||(X.parentNode.insertBefore(d,X),W(b,0))}}(this,document),Modernizr.load=function(){yepnope.apply(window,[].slice.call(arguments,0))};