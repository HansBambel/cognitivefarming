# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:05:49 2016

@author: Valentin
"""

from bs4 import BeautifulSoup

html_doc = """

<html>
  <head>
    <title>
      Abstandsauflagen
    </title>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="site.css" rel="stylesheet" type="text/css">
    <style type="text/css">
      <!--
      .Stil2 {font-family: Verdana, Arial, Helvetica, sans-serif; font-size: xx-small;}
      .Stil3 {font-family: Verdana, Arial, Helvetica, sans-serif; font-size: xx-small; font-weight: bold}
      .Stil4 {font-family: Verdana, Arial, Helvetica, sans-serif; font-size: xx-small; text-decoration:none;}
      .Stil5 {font-family: Verdana, Arial, Helvetica, sans-serif; font-size: small; text-decoration:none;}
       @media print { 
        .noprint { display:none; }
       } 
       @media screen { 
        .noscreen { display:none; }
       } 
      -->
    </style>
    <script type="text/javascript">
    function FensterOeffnen (Adresse) {
      MeinFenster = window.open(Adresse, "Zweitfenster", "width=400,height=280,left=500,top=300,scrollbars=no,dependent=yes");
      MeinFenster.focus();
    }
    </script>
  </head>
  <body >
<h1>Regierungspr�sidium Gie�en - Pflanzenschutzdienst Hessen<img style="float: right; margin-right: 30px;" src="rpgi50.jpg" alt="rpgi50" height="22" width="50" /></h1>
<h2>Abstandsauflagen</h2>
 
    
  <div class='noprint'>
  <form name='mf' action='/ausgabe/aa/aa_ausgabe_mk.php' method='POST'>  
  <input type="hidden" name="sent" value="yes">
  <p class="Stil5">
  Produktname (Eingabe der Anfangsbuchstaben gen&uuml;gt):
    <input type="text" name="produkt" id="produkt" value=""  />
  <p class="Stil5"><b>oder</b>
  <p class="Stil5">Pflanzenschutzmittelgruppe:&nbsp;
  <select name='psmart' size='1' class='normalMasken' id='psmart' value='$mpsmart'>
    <option  value="alle" >alle</option>
    <option  value="Getreidefungizid" >Getreidefungizide</option>
    <option  value="Getreideherbizid" >Getreideherbizide</option>
    <option  value="Wachstumsregler Getreide" >Wachstumsregler Getreide</option>
    <option  value="Maisherbizid" >Maisherbizide</option>
    <option  value="Maisfungizid" >Maisfungizide</option>
    <option  value="Insektizid" >Insektizide</option>
    <option  value="Rapsherbizid" >Rapsherbizide</option>
    <option  value="Rapsfungizid, -wachstumsregler oder -insektizid" >Rapsfungizide, -wachstumsregler oder -insektizide</option>
    <option  value="Schneckenkorn" >Schneckenkorn</option>
    <option  value="Kartoffelherbizid" >Kartoffelherbizide</option>
    <option  value="Kartoffelfungizid" >Kartoffelfungizide</option>
    <option  value="R�benherbizid" >R�benherbizide</option>
    <option  value="R�benfungizid" >R�benfungizide</option>
    <option  value="Herbizid in AB, FE und LU" >Herbizide in Ackerbohnen, Futtererbsen und Lupinen</option>
    <option  value="Fungizid in AB, FE und LU" >Fungizide in Ackerbohnen, Futtererbsen und Lupinen</option>
    <option  value="Totalherbizid" >Totalherbizide</option>
    <option  value="Gr�nlandherbizid" >Gr�nlandherbizide</option>
  </select>
  <p class="Stil5">Liegt die Fl�che in einer Gemeinde mit ausreichend Kleinstrukturen oder ist die Saumstruktur < 3 m?
  <input type="radio" name="kleinstrukturiert" value="1" >ja
  <input type="radio" name="kleinstrukturiert" value="2" checked="checked">nein</p>
  <p class="Stil5">Gemeinden mit <b>nicht</b> ausreichendem Anteil an Kleinstrukturen in Hessen sind zum 01. Februar 2014: <br>Gernsheim, Espenau, Grebenstein, Niederdorfelden, Ederm�nde, Gudensberg, Karben, Niddatal, W�lfersheim, W�llstadt.</p>
  <input type='submit' name='suche' value='Suchen' class='normalMasken'>
  </div>
  </form>
  </p>
          
<div class='noscreen'>
<h2>Auswahl:</h2> 
<p class="Stil5">Pflanzenschutzmittelgruppe: alle<p class='Stil5'>Gemeinde mit <b>nicht</b> ausreichendem Anteil an Kleinstrukturen oder Saum <b>nicht</b> kleiner 3 m</div>

<table width="98%" border="0">
  <tr> 
    <td class="Topic" width="98%"> 
      <!--Abstandsauflagen&nbsp;--><a href='javascript:window.print()'><img  class='noprint' src='printButton.png' border=0 width='14' height='14'></a>
    </td>
  </tr>
  <tr> 
    <td class="Stil2"> 
      <table border="1" cellpadding="2" cellspacing="0">
    <tr bgcolor="#ADCAE5">
      <td style="text-align: center;" class="Stil2" colspan="1" rowspan="9">Produkt<br><br>(H) = Herbstanwendung<br>(F) = Fr&uuml;hjahrsanwendung<br><br>Stand: 09.11.2016</td>
      <td style="text-align: center;" class="Stil2"  colspan="1" rowspan="9">Aufwand-<br>menge<br>l oder kg /ha</td>
      <td style="text-align: center;" class="Stil2"  colspan="1" rowspan="9">Gew&auml;sser bezogene Auflagen</td>
      <td style="text-align: center;" class="Stil2"  colspan="10" rowspan="1">Abstandsangaben in Meter</td>
    </tr>
    <tr bgcolor="#ADCAE5">
      <td style="text-align: center;" class="Stil2"  colspan="5" rowspan="1">Gew&auml;sser</td>
      <td style="text-align: center;" class="Stil2"  colspan="1" rowspan="8">Saum-<br>struktur <br>bezogene <br>Auflagen</td>
      <td style="text-align: center;" class="Stil2"  colspan="4" rowspan="1">Saumstruktur</td>
    </tr>
    <tr bgcolor="#ADCAE5">
      <td style="text-align: center;">&nbsp;</td>
      <td style="text-align: center;" class="Stil2"  colspan="3" rowspan="4">bei Abdrift-<br>minderung von</td>
      <td style="text-align: center;" class="Stil2"  colspan="1" rowspan="7">wenn <br>Hang-<br>nei-<br>gung <br>&gt; 2%</td>
      <td style='text-align: center;' class='Stil2'  colspan='4' rowspan='4'>In Kleinstrukturge-<br>bieten oder Saum &lt; 3m <br>ist NT 101, 102, 103 <br>nicht relevant und bei <br>NT 107, 108, 109 <br>kann man 5 m abziehen</td>    </tr>
    <tr align="center" bgcolor="#ADCAE5">
      <td>&nbsp;</td>
    </tr>
    <tr align="center" bgcolor="#ADCAE5">
      <td>&nbsp;</td>
    </tr>
    <tr align="center" bgcolor="#ADCAE5">
      <td>&nbsp;</td>
    </tr>
    <tr bgcolor="#ADCAE5">
      <td style="text-align: center;" class="Stil2"  colspan="1" rowspan="3">Stan-<br>dard-<br>d&uuml;se</td>
      <td style="text-align: center;" class="Stil2"  rowspan="3" colspan="1">50 %</td>
      <td style="text-align: center;" class="Stil2"  rowspan="3" colspan="1">75 %</td>
      <td style="text-align: center;" class="Stil2"  colspan="1" rowspan="3">90 %</td>
      <td style="text-align: center;" class="Stil2"  colspan="1" rowspan="3">Stan-<br>dard-<br>d&uuml;se</td>
      <td style="text-align: center;" class="Stil2"  colspan="3" rowspan="1">bei Abdriftmin-</td>
    </tr>
    <tr align="center" bgcolor="#ADCAE5">
      <td  class="Stil2" colspan="3" rowspan="1">derung von</td>
    </tr>
    <tr bgcolor="#ADCAE5">
      <td style="text-align: center;" class="Stil2" >50 %</td>
      <td style="text-align: center;" class="Stil2" >75 %</td>
      <td style="text-align: center;" class="Stil2" >90 %</td>
    </tr>
        <tr>
            <td class='Stil2' colspan='13' bgcolor=#F4C300><b>Getreidefungizide</b></td>
          </tr>                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Acanto (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Achat (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Adexar (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 609, 706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Agent (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Alto 240 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,4 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Amistar (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Amistar Opti (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 607, 701, NG 331 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ampera (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1/ 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aviator Xpro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,00 
            </td>
            <td class="Stil2" align="left"> NW 605-1/606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aviator Xpro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 605-1/606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bayfidan (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bontima (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701, NG 342-1 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bravo 500 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 607, NW 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Capalo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Caramba (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ceralo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ceralo (zur Weizenbl�te) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ceriax (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Champion (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cirkon (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Corbel (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Credo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 607, 706, NG 331 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Diamant (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,75 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Domark 10 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Don-Q (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,1 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Eleando (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Emerald (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Epoxion (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Epoxion Top (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 706, 712 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fandango (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Flamenco FS (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,3 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Flexity (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Folicur (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 - 1,25 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fortress (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gladio (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 706, 712 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gladio (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 706, 712 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Input Classic (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 607, 706 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Input Classic (gegen Fusarium) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Input Xpro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 607, 706 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Juwel Forte (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Juwel Top (Sommergetreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 705 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Juwel Top (Wintergetreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Kantik (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1, NW706, NW 712 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Matador  (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mirage 450 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 705 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Opus Top (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Orius (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Osiris (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Proline (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pronto Plus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 607, 706 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Prosaro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Seguris (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701, NG 342-1 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Seguris Xtra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606, NG 342-1 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Siltra Xpro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Skyway Xpro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Skyway Xpro (gegen Fusarium) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Soleil (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sportak 45 EW (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stratego (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stratego (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sympara (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Talius (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Taspa (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tilt 250 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Torero (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Variano Xpro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,75 
            </td>
            <td class="Stil2" align="left"> NW 605-1/606, 705 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Vegas (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,375 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Viverda (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW605-1, NW606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Zenit M  (Hafer)  (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Zenit M (Gerste, Weizen) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreidefungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 01 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Getreideherbizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Absolute M (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 0,18 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Activus SC (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 4 
            </td>
            <td class="Stil2" align="left"> NW 607-1,705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Acupro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Acupro (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,065 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Addition (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 706, 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Alliance (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Alliance (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,065 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Amario (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aniten Super (Hafer, S-Gerste) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, NG 403, 404 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Antarktis (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 607-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Antarktis (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Arelon fl&uuml;ssig (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706, NG 405, 410, 411 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Arelon fl&uuml;ssig (F/H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F/H--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605, NW 606, 706, NG 404, 405, 410, 411 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ariane C (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Artus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,050 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis OD (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis OD (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis OD (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis OD (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 609,701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis OD (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis OD (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 701 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 701, NW 800 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis WG (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis WG (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,4 
            </td>
            <td class="Stil2" align="left"> NW 701 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlantis WG (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 701 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Atlanti�s OD (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701, 800 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Attribut (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,06-0,1 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Axclean (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Axclean (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,075 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Axial 50 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Axial 50 (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 0,9 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Axial Komplett (F/H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F/H--> 
            </td>
            <td class="Stil2" align="center"> 1,3 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Azur (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, NG 402,410,411 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bacara forte NA (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bacara forte VA (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701, 800 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bacara forte VA/NA (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Basagran DP (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NG 315, 407, 412,413, 711 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> BeFlex (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Biathlon (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,07 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Biathlon 4 D (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,07 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Biathlon 4 D (mit Dash) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,07 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Boxer (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Brazzos (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,025 
            </td>
            <td class="Stil2" align="left"> NW 606/606,706,800 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Broadway (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,275 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Broadway (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,13 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cadou Forte Set (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,75 + 0,3 
            </td>
            <td class="Stil2" align="left"> NW701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cadou SC (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 701 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cadou SC (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,3 VA 
            </td>
            <td class="Stil2" align="left"> NW 705 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cadou SC (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,24 NA 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Caliban Duo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,33 
            </td>
            <td class="Stil2" align="left"> NW 705 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Caliban Top (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,30 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Carmina 640 (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, NG 337, 404, 405, 414 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Carmina 640 (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, NG 337, 404, 405, 414 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ciral / Corporal (F/H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F/H--> 
            </td>
            <td class="Stil2" align="center"> 0,025 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Concert SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706, 800 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Concert SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,10 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701, 800 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Diflanil 500 SC (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,375 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 706, 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Dirigent SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,035 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Duanti ( - BBCH 39) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,75 
            </td>
            <td class="Stil2" align="left"> NW605-1, NW606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Duanti (- BBCH 32) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,000 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Duplosan DP, Lotus DP (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,33 
            </td>
            <td class="Stil2" align="left"> NW 609-1, NW 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Duplosan KV (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NG314, NG402 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ergon (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,07 
            </td>
            <td class="Stil2" align="left"> NW 605-1/606, 706, 800 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Falkon (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605-1/606,706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fenikan (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, NG 404, 405, 410, 411 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fenikan (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3 
            </td>
            <td class="Stil2" align="left"> NG 404,405,410,411, NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Filon (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Finy (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,04 
            </td>
            <td class="Stil2" align="left"> NW 609, NW 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fluroxane (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Follow  (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fox (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gropper SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,04 
            </td>
            <td class="Stil2" align="left"> NW609, NW701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Herbaflex (F/H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F/H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706, NG 405 ,410, 411 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Herold SC (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> NW 706,607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Hoestar Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Hoestar Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Husar OD (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,075-0,1 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Husar Plus + Mero (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 + 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 800 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lentipur 700 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, NG 337, 404, 405 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lentipur 700 (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, NG 337, 404 ,405, 414 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lexus (F/H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F/H--> 
            </td>
            <td class="Stil2" align="center"> 0,02 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lodin EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lotus Pixie (Sommergetreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NG 404, NW 605, 606, 800 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lotus Pixie (Wintergetreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NG 404, 405, NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Malibu (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 4 
            </td>
            <td class="Stil2" align="left"> NW 605-1,NW 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT112, NT145, NT 146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pelican Delta (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606, NW701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Picona (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3 
            </td>
            <td class="Stil2" align="left"> NW 605-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Platform S (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pointer Plus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pointer SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,06 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pointer SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,045 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pointer SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,0375 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pointer SX (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,03 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Primus Perfekt (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Protugan (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, NG 404, 405, 410, 411 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Protugan (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, NG 404, 405, 410, 411 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ralon Super (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 701 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ralon Super (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 701, 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Saracen (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Starane XL (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,8 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 4,4 
            </td>
            <td class="Stil2" align="left"> NW 607-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sumimax (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,06 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sword (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Toluron 700 SC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, NG 337, 404, 405 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Toluron 700 SC (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706,  NG 337, 404, 405, 414 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tomigan 180 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tomigan 200 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,9 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Topik 100 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Topik 100 (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Traxos (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Trimmer SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,06 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Trimmer SX (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 0,03 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Trinity (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 607, 706, 800, NG 337 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 101, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Troller (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Troller (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,075 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> U 46 D- Fluid (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> U 46 M- Fluid (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Vertix (F/H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> F/H--> 
            </td>
            <td class="Stil2" align="center"> 0,08 
            </td>
            <td class="Stil2" align="left"> NW605, NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Vertix (H/F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H/F--> 
            </td>
            <td class="Stil2" align="center"> 0,08 
            </td>
            <td class="Stil2" align="left"> NW605, NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Viper Compact (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1, NW 706, NW 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Zoom (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Getreideherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 02 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 605-1. NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Wachstumsregler Getreide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bogota Ge (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Calma (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Camposan-Extra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,1 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> CCC 720 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> CCC 720  in Weizen (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,1 
            </td>
            <td class="Stil2" align="left"> NG 412 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cerone 660 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,1 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Countdown (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Medax Top (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Moddus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Moddus Start (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Wachstumsregler Getreide 
            </td>
            <td class="Stil2" align="left">&nbsp; 03 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Maisherbizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Activus SC  (VA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 145, NT 146, NT 170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Activus SC ( NA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 145, NT 146, NT 170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Arigo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,33 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, NG 200, 326-1, 327 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Arrat (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Artett (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NW 603 NG 315, 402, 407,413, 711 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aspect (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> B 235 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 705 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bromoterb (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606,NG 402 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bromotril 225 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606,  705 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bromoxynil 235 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606,  705 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Buctril (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 705, 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Calaris (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, NG 402 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Callisto, Maran, Mesotrione 100 SC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Caracho 235 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606. 705 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Casper (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cato (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Certrol B (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 705 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cirontil (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,44 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, NG 200, 326-1, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Clio (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NG 323 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Clio Star (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NG 323 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Clio Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 323 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cliophar 100 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Dual Gold (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 609, NG 402 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Effigo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,35 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Elumis (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, NG 200, 326, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> ESCEP (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gardo Gold (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4 
            </td>
            <td class="Stil2" align="left"> NW 609, NG 402 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gardobuc (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, NG 402 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Harmony SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,015 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Kelvin (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 200, 326, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Laudis (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,25 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Laudis WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lontrel 600 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lontrel 720 SG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,167 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mais-Banvel WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Maister fl�ssig (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,50 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> MaisTer power (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,50 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, 800 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Maister power (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606, NW 706, NW 800 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> MaisTer power (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, 800 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mikado (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 705 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Milagro Forte (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 200, 326, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Motivell Forte (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 200, 326, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Nicogan (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 200, 326, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Peak (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,02 
            </td>
            <td class="Stil2" align="left"> NW 701, 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Principal (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,075 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 200, 326-1, 327 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Quantum (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706, NG 405 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Rosan (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Samson 4 SC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, NG 200, 326-1, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Samson EXTRA 6 OD (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 200, 326, 327 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Spectrum (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,4 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Spectrum Gold (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, NG 405 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Spectrum Gold (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua   (VA, NA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua  (NA, VA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,4 
            </td>
            <td class="Stil2" align="left"> NW 607-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Successor T (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1/606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sulcogan (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT  101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tacco (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706, NG 405 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Task + Trend (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,383 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Terano fl�ssig (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Titus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 x 80 g 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Titus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 40 g 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Xinca (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Zeagran Ultimate (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Maisfungizide</b></td>
          </tr>
                                                  <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Quilt Xcel (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04a 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606, NW 705 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Retengo Plus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04a 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5(30-39) 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Retengo Plus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Maisfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 04a 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5(51-65) 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Insektizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Actara (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Alverde  (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> NW 605,606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Avaunt (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,17 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bi 58, Danadim Progress, Perfe (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,4 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bi 58, Danadim Progress, Perfe (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,7 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Biscaya (Getreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Biscaya (Raps) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bulldock (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Coragen ( Kartoffeln) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,06 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Coragen (Mais) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,125 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Dantop (Kartoffeln, Legen) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NG 321 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Dantop in Kartoffeln (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,035 
            </td>
            <td class="Stil2" align="left"> NG 321 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Dantop, (Kartoffeln) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701, NG 321 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis fl�ssig (Getreide) (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis fl�ssig (Getreide, Raps) (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 607, NW705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis fl�ssig (Kartoffel, Raps) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis fl�ssig (Vektoren Getreide)  (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis fl�ssig (Z.R�ben) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis forte (Getreide-Wickler) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,075 
            </td>
            <td class="Stil2" align="left"> NW 607-1, NW 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis forte (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> NW 607-1, NW 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis forte (L�use, Kohlschotenm...) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Decis forte (Wiese) (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> NW 607-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fastac SC (Getreide) (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,125 
            </td>
            <td class="Stil2" align="left"> NW 607, 607-1, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fastac SC (Getreide, R�be) (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fastac SC (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,065 
            </td>
            <td class="Stil2" align="left"> NW 705, 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fastac SC S.G.(Getreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 701, 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fastac SC.(Raps) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fury 10 EW (Getreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fury 10 EW (Raps) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,1 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Kaiso Sorbie (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Karate Zeon  (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,075 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mavrik (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mospilan SG ( Raps, Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> NeemAzal T/S (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Nexide      (Getreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 0,08 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Nexide      (Raps) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 0,08 
            </td>
            <td class="Stil2" align="left"> NW 607, 705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pirimor Granulat (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,30 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pirimor Granulat (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,45 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Plenum 50 WG (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Plenum 50 WG (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Plenum 50 WG (Raps) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Shock DOWN (Getreide) (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Shock DOWN (Kartoffel, Raps, Z.R�ben) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Spintor  (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 0,05 
            </td>
            <td class="Stil2" align="left"> NW 606/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Spintor (Mais) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Steward  (Mais) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,125 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sumi Alpha 5 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> NW 607, NW 706 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sumicidin Alpha (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 607, 706 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sumicidin Alpha EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> NW 706, 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sumicidin Alpha EC (Getreide) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 706, 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Teppeki (Kartoffel) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,16 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Teppeki (Weizen) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,14 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Trafo WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,15 
            </td>
            <td class="Stil2" align="left"> NW 605-1/606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Trebon 30 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 05 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Rapsherbizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Agil- S (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Agil-S (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aramo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aramo (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bengala (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, NG 346 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 127, 145, 146, 149, 152, 153, 155 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Brasan (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 127, 145, 146, 149, 152, 153, 155 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Butisan (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605,606, 706, NG 346 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Butisan Gold (im VA+NA) (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706, NG 346 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Butisan Kombi (VA, NA) (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706, NG 346 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Butisan Top (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 346 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Centium 36 CS (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,33 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 127, 145, 146, 149, 152, 153, 154 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cirrus (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,24 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 127, 145, 146, 149, 152, 153, 154 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cohort (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,875 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT  102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Colzor Trio (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 4 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 127, 145, 146, 149, 152, 153, 155 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Colzor Uno (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 705, NG 334, NG 335 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> CS 36 (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,33 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 127, 145, 146, 149, 152, 153, 154 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Devrinol Fl. (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,75 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Echelon (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,24 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT127, NT 145, 146, 149, 152, 153, 154 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Effigo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,35 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Effigo (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,35 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fox (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 609,701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fox (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,3+0,7 
            </td>
            <td class="Stil2" align="left"> NW 605/606,706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fuego (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606,706, NG 346 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fuego Top (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706, NG 343, 346 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gamit 36 CS (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,33 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 127, 145, 146, 149, 152, 153, 154 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Groove (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,875 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT  101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Katamaran Plus (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Kerb 50 W (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Kerb Flo (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,875 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Kerb Flo (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lontrel 600 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lontrel 720 SG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,167 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Milestone (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Nimbus CS (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 3 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 346 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 127. 145, 146, 149, 152, 153, 155 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Quantum (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 405 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglone (Winterraps, Sikkation) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Runway (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,2 
            </td>
            <td class="Stil2" align="left"> NG349, NG350 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Select 240 EC + Actirob (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 706 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua (VA) (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Raps (NA) (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Vivendi 100 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 06 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Rapsfungizide, -wachstumsregler oder -insektizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Acanto (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW605-1, NW606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ampera (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cantus (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cantus Gold (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cantus Gold  (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Caramba (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Carax (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,4 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cercobin FL (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Contans WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Custodia (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Efilor (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Folicur (H) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> H--> 
            </td>
            <td class="Stil2" align="center"> 1 
            </td>
            <td class="Stil2" align="left"> NW 605,606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Folicur (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Matador (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mirage 450 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Moddus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Orius (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ortiva (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Proline (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,7 
            </td>
            <td class="Stil2" align="left"> NW 609, 705 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Propulse (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Prosaro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Symetra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, NG 342-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tilmor (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Toprex (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Rapsfungizid, -wachstumsregler oder -insektizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 07 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, NG 341 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Schneckenkorn</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Arinex (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 6,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Delicia Schneckenlinsen (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ferramol Schneckenkorn (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 25,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Metarex Inov (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Metarex TDS (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 7,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mollustop (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Patrol MetaPads (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pro Limax (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Schneckenkorn Spiess-Urania (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sluxx HP (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Schneckenkorn 
            </td>
            <td class="Stil2" align="left">&nbsp; 08 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 7,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Kartoffelherbizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Agil-S (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aramo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Artist (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Artist (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 706, 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bandur (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 701, 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Boxer (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT145, NT 146, NT 170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cato (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Centium 36 CS (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102, NT 127, NT 149 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> ESCEP (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,05 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mistral (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Mistral (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Novitron DamTec (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,4, VA 
            </td>
            <td class="Stil2" align="left"> NW607-1, NW701 
            </td>
            <td class="Stil2" align="center"> 99 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Quickdown (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 0,8 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglone (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglone (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglone (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Select 240 EC + Actirob (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 706 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Select 240 EC + Actirob (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 706 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sencor liquid (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,9 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sencor liquid (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> NW 609-1, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sencor WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 706, 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sencor WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> NW 706, 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Shark (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tacco (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,3 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 706, NG 405 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Titus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2 x 40 g 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Titus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 09 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 x 80 g 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Kartoffelfungizide</b></td>
          </tr>
                                                  <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Acrobat Plus WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Areva MZ (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Banjo Forte (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bravo 500 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 706, 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Canvas (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Carial Flex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Carneol (=Banjo) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,4 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Contans WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 8,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cueva (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 8,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cuprozin progress (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Dithane Neo Tec (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,8 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Electis (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,8 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> &nbsp; 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Epok (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 607, 701 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fantic M (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gemini (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Infinito (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,6 
            </td>
            <td class="Stil2" align="left"> NW 609, NG 324-2, 325 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Infinito (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> NG 324-2, 325 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ortiva (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ortiva (beim Legen) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, NG 340-1, 405 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Polyram WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,8 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ranman Top (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Revus Top (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Revus Top (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ridomil Gold MZ (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Shaktis (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Shirlan (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,4 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Signum (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> SYD 11640 H (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NW607-1, NW706, NG405 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tanos (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,7 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tattoo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tattoo C (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,7 
            </td>
            <td class="Stil2" align="left"> NW 607, 706 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Terminus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,4 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Valbon (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,6 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Valis M (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Vondac DG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Zampro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,8 
            </td>
            <td class="Stil2" align="left"> NG 339 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Zetanil M (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Kartoffelfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 10 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>R�benherbizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aabetam Tandem (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 607-1, NG 405 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Agil-S (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Aramo (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Asket 470 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,66 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Belvedere Extra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3 x 1,3 
            </td>
            <td class="Stil2" align="left"> NW 609-1, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betanal Expert (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 701 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betanal MAXXPRO (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,5 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betanal Quattro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betasana Trio (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 706 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betosip SC, Betasana SC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3 x 2,0 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betosip SC, Betasana SC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1 x 6,0 
            </td>
            <td class="Stil2" align="left"> NW 607 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betoxon 65 WDG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NG 301, 402, 415 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Betoxon 65 WDG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NG 301, 404, 415 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cliophar 100 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Completto (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3 x 3-4 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Debut (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,03 
            </td>
            <td class="Stil2" align="left"> NW 609-1 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ethosat 500 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NG 402 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Goltix Gold (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NG 404 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Goltix Titan (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NG 343, NG 404 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lontrel 600 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Lontrel 720 SG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,167 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Pyramin WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NG 404, 407 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Rebell (NA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, NG 402, 407 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Rebell (VA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NG 402, 407 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Rebell Ultra (NA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3 x 0,83 
            </td>
            <td class="Stil2" align="left"> NW 609-1, NG 343, 402 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Rebell Ultra (VA) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NG 343, 402 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Safari (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,04 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Select 240 EC + Actirob (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> NW 706 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Select 240 EC + Actirob (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 706 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> NT109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Spectrum (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,9 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Targa Super (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Terlin DF+ T.WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NG 404,  407 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Terlin DF+ T.WG (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NG 402, 407 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Tramat 500 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,66 
            </td>
            <td class="Stil2" align="left"> NG 412 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Vivendi 100 (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 11 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,2 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>R�benfungizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Amistar (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Cirkon (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Domark 10 EC (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Duett Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,6 
            </td>
            <td class="Stil2" align="left"> NW 605/606, 706 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Emerald (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fortress (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Juwel (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,00 
            </td>
            <td class="Stil2" align="left"> NW 701, 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Opus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,00 
            </td>
            <td class="Stil2" align="left"> NW 701, 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ortiva (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,00 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 705 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Rubric (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, NW 606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Score (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,4 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Sphere (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,7 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Spyrale (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; R�benfungizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 12 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 603 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Herbizide in Ackerbohnen, Futtererbsen und Lupinen</b></td>
          </tr>
                                                  <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Agil-S  (AB + FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,75 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Bandur (AB + FE ) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NW 607-1, 701, 800 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Basagran (AB) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NG 315, 407, 413, 711 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Basagran (FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NG 315, 402, 407, 413, 711 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Boxer (AB, FE, LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 145, NT 146, NT 170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Centium 36 CS (AB + FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102, 127, 149 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Focus Ultra (FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max ( FE, LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0  
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Fusilade Max (AB,FE, LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Gardo Gold (LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,0 
            </td>
            <td class="Stil2" align="left"> NW 609, NG 402 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Novitron DamTec( AB, FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,4, VA 
            </td>
            <td class="Stil2" align="left"> NW607-1, NW701 
            </td>
            <td class="Stil2" align="center"> 99 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex  (AB + FE ) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Panarex  (AB + FE ) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglone (AB+FE, Sikkation) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Select 240 EC + Actirob (nur LUP) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Select 240 EC + Actirob(nur FE Saat) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stallion SynTec (AB + FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW607-1, NW705 
            </td>
            <td class="Stil2" align="center"> 99 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT109, NW127,NT145, NT146, NW149, NT170 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua (VA) (AB, FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,5 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 705 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua (VA) (AB, FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 4,4 
            </td>
            <td class="Stil2" align="left"> NW 607-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Stomp Aqua (VA) (LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Herbizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 13 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,6 
            </td>
            <td class="Stil2" align="left"> NW 605-1 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 112, NT145, NT146, NT170 
            </td>
                        <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> nein 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Fungizide in Ackerbohnen, Futtererbsen und Lupinen</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Amistar (AB, FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Fungizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 14 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 609, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Contans WG (AB) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Fungizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 14 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 - 8,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Folicur    (AB, FE, LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Fungizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 14 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605-1, 606, 701 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ortiva (AB, LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Fungizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 14 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 701 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ortiva (FE) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Fungizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 14 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606, 705 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Switch   (LU) (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Fungizid in AB, FE und LU 
            </td>
            <td class="Stil2" align="left">&nbsp; 14 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,0 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Totalherbizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Berghoff Glyphosate Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor="#ADCAE5"> 
            <td class=stil3> <div valign="top" align="left">Produkt</div></td>
            <td class=stil3> <div align="center">Menge</div></td>
            <td class=stil3> <div align="center">Gew&auml;sserauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
            <td class=stil3> <div align="center">Hang</div></td>
            <td class=stil3> <div align="center">Saumauflagen</div></td>
            <td class=stil3> <div align="center">Std.</div></td>
            <td class=stil3> <div align="center">50 %</div></td>
            <td class=stil3> <div align="center">75 %</div></td>
            <td class=stil3> <div align="center">90 %</div></td>
         </tr>
                    <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Dominator Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Glyfos Dakar (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 1,6 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Glyfos Supreme (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,4 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Glyphos TF Classic (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Kyleo (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NW605-1, 606, NG 352 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglone (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 15 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Reglone (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NW 605, 606 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Roundup PowerFlex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,75 
            </td>
            <td class="Stil2" align="left"> NG 352, NG 402 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Roundup PowerFlex (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 3,75 
            </td>
            <td class="Stil2" align="left"> NG 402, 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Roundup REKORD (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NG 352, NG 402 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Roundup Rekord (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,5 
            </td>
            <td class="Stil2" align="left"> NG 352, 402 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Roundup Solid (HF) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> HF--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Roundup Turbo Plus (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,65 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 102 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Roundup Ultra (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Touchdown Quattro (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Totalherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 15 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 5,0 
            </td>
            <td class="Stil2" align="left"> NG 352 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 101 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                      <tr>
            <td class="Stil2" colspan="13" bgcolor=#F4C300><b>Gr�nlandherbizide</b></td>
          </tr>
                                                  <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Banvel M (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 6,0 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Duplosan KV (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> NG 314, 402 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="left"> NT 109 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Garlon  (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Garlon Premium (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW 609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Genoxone ZX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 6,25 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Harmony SX (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 0,045 
            </td>
            <td class="Stil2" align="left"> NW 605/606 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Ranger (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW609 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Simplex (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> NW605-1, NW606 
            </td>
            <td class="Stil2" align="center"> 10 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> Starane Ranger (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 3,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 103 
            </td>
                        <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 20 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr bgcolor=#D3DDF3 > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> U 46 D-Fluid (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
                        <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
             </tr>
                                                <tr  > 
            <td width="8%" class="Stil2" nowrap > <div align="left"> 
                <span class="Stil2"> U 46 M Fluid (F) 
                </span></div></td>
            <!--<td class="Stil2" align="left">&nbsp; Gr�nlandherbizid 
            </td>
            <td class="Stil2" align="left">&nbsp; 16 
            </td>
            <td class="Stil3" align="center"> F--> 
            </td>
            <td class="Stil2" align="center"> 2,0 
            </td>
            <td class="Stil2" align="left"> - 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="center"> 0 
            </td>
            <td class="Stil2" align="left"> NT 108 
            </td>
                        <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 25 
            </td>
            <td class="Stil2" align="center"> 5 
            </td>
             </tr>
              </table>
    </td>
  </tr>
    
  <tr>
    <td colspan="19" class="Stil4"><div class="noscreen">Bearbeiter: Eberhard Cramer, Am Versuchsfeld 17, 34128 Kassel, Tel. 0561 9888455, eberhard.cramer@rpgi.hessen.de</div></td>
  </tr>
    
</table>
</body>
</html>
"""

#def get_tables():
#    soup = BeautifulSoup(open(r'C:\Users\Valentin\Uni\Hackathon\Abstandsauflagen\Abstandsauflagen_Hessen.hmt'))
#    return soup.findAll('table')
#    
def makelist(table):
  result = []
  allrows = table.find_all('tr')
  for row in allrows:
    result.append([])
    allrows2 = row.find_all('tr')
    for row2 in allrows2:
        allcols = row2.find_all('td')
        for col in allcols:
          thetext = col.string
          result[-1].append(thetext)
  return result
  

  
test = BeautifulSoup(html_doc,'html.parser')

results = makelist(test.table.table)
