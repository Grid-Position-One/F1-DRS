// ============================================================
//  F1-DRS DATA LAYER
//  本文件由 scripts/update_data.py 自动生成，请勿手动编辑。
//  手动修改请改 index.html 后重新提取，或直接编辑本文件后运行脚本。
// ============================================================

// ===== circuits =====
const circuits = [
  { no:'1', gp:'澳大利亚大奖赛', circuit:'Albert Park', city:'墨尔本', date:'3月6-8日', trackDetailId:1 },
  { no:'2', gp:'中国大奖赛', circuit:'Shanghai International Circuit', city:'上海', date:'3月13-15日 (冲刺赛)', trackDetailId:2 },
  { no:'3', gp:'日本大奖赛', circuit:'Suzuka Circuit', city:'铃鹿', date:'3月27-29日', trackDetailId:3 },
  { no:'—', gp:'巴林大奖赛', circuit:'Bahrain International Circuit', city:'萨基尔', date:'4月10-12日 ❌取消', trackDetailId:4 },
  { no:'—', gp:'沙特阿拉伯大奖赛', circuit:'Jeddah Corniche Circuit', city:'吉达', date:'4月17-19日 ❌取消', trackDetailId:5 },
  { no:'4', gp:'迈阿密大奖赛', circuit:'Miami International Autodrome', city:'迈阿密', date:'5月1-3日 (冲刺赛)', trackDetailId:6 },
  { no:'5', gp:'加拿大大奖赛', circuit:'Circuit Gilles Villeneuve', city:'蒙特利尔', date:'5月22-24日', trackDetailId:10 },
  { no:'6', gp:'摩纳哥大奖赛', circuit:'Circuit de Monaco', city:'蒙特卡洛', date:'6月5-7日', trackDetailId:8 },
  { no:'7', gp:'巴塞罗那-加泰罗尼亚大奖赛', circuit:'Circuit de Barcelona-Catalunya', city:'巴塞罗那', date:'6月12-14日', trackDetailId:9 },
  { no:'8', gp:'奥地利大奖赛', circuit:'Red Bull Ring', city:'斯皮尔伯格', date:'6月26-28日', trackDetailId:11 },
  { no:'9', gp:'英国大奖赛', circuit:'Silverstone Circuit', city:'银石', date:'7月3-5日 (冲刺赛)', trackDetailId:12 },
  { no:'10', gp:'比利时大奖赛', circuit:'Circuit de Spa-Francorchamps', city:'斯帕', date:'7月17-19日', trackDetailId:13 },
  { no:'11', gp:'匈牙利大奖赛', circuit:'Hungaroring', city:'布达佩斯', date:'7月24-26日', trackDetailId:14 },
  { no:'12', gp:'荷兰大奖赛', circuit:'Circuit Zandvoort', city:'赞德沃特', date:'8月21-23日 (冲刺赛)', trackDetailId:15 },
  { no:'13', gp:'意大利大奖赛', circuit:'Autodromo Nazionale Monza', city:'蒙扎', date:'9月4-6日', trackDetailId:16 },
  { no:'14', gp:'西班牙大奖赛', circuit:'Madrid Street Circuit 🆕', city:'马德里', date:'9月11-13日', trackDetailId:0 },
  { no:'15', gp:'阿塞拜疆大奖赛', circuit:'Baku City Circuit', city:'巴库', date:'9月24-26日', trackDetailId:17 },
  { no:'16', gp:'新加坡大奖赛', circuit:'Marina Bay Street Circuit', city:'新加坡', date:'10月9-11日 (冲刺赛)', trackDetailId:18 },
  { no:'17', gp:'美国大奖赛', circuit:'Circuit of the Americas', city:'奥斯汀', date:'10月23-25日', trackDetailId:19 },
  { no:'18', gp:'墨西哥城大奖赛', circuit:'Autódromo Hermanos Rodríguez', city:'墨西哥城', date:'10月30日-11月1日', trackDetailId:20 },
  { no:'19', gp:'圣保罗大奖赛', circuit:'Autódromo José Carlos Pace', city:'圣保罗', date:'11月6-8日', trackDetailId:21 },
  { no:'20', gp:'拉斯维加斯大奖赛', circuit:'Las Vegas Strip Circuit', city:'拉斯维加斯', date:'11月19-21日', trackDetailId:22 },
  { no:'21', gp:'卡塔尔大奖赛', circuit:'Lusail International Circuit', city:'卢赛尔', date:'11月27-29日', trackDetailId:23 },
  { no:'22', gp:'阿布扎比大奖赛', circuit:'Yas Marina Circuit', city:'阿布扎比', date:'12月4-6日', trackDetailId:24 }
];

// ===== compareDrivers =====
const compareDrivers = [
  { name:"Max Verstappen", nat:"荷兰", age:28, num:1, team:"Red Bull Racing", teammate:"Isack Hadjar", races:224, wins:63, poles:40, best:"世界冠军×4", rank2025:"第2" },
  { name:"Isack Hadjar", nat:"法国", age:21, num:6, team:"Red Bull Racing", teammate:"Max Verstappen", races:9, wins:0, poles:0, best:"新秀", rank2025:"F2冠军" },
  { name:"Lando Norris", nat:"英国", age:26, num:4, team:"McLaren", teammate:"Oscar Piastri", races:148, wins:5, poles:9, best:"第2名", rank2025:"第1（世界冠军）" },
  { name:"Oscar Piastri", nat:"澳大利亚", age:25, num:81, team:"McLaren", teammate:"Lando Norris", races:72, wins:3, poles:2, best:"第2名", rank2025:"第3" },
  { name:"Charles Leclerc", nat:"摩纳哥", age:28, num:16, team:"Ferrari", teammate:"Lewis Hamilton", races:170, wins:9, poles:26, best:"第2名", rank2025:"第4" },
  { name:"Lewis Hamilton", nat:"英国", age:41, num:44, team:"Ferrari", teammate:"Charles Leclerc", races:362, wins:105, poles:104, best:"世界冠军×7", rank2025:"第6" },
  { name:"George Russell", nat:"英国", age:28, num:63, team:"Mercedes", teammate:"Kimi Antonelli", races:148, wins:3, poles:3, best:"第4名", rank2025:"第5" },
  { name:"Kimi Antonelli", nat:"意大利", age:19, num:12, team:"Mercedes", teammate:"George Russell", races:9, wins:5, poles:0, best:"新秀", rank2025:"F2" },
  { name:"Fernando Alonso", nat:"西班牙", age:44, num:14, team:"Aston Martin", teammate:"Lance Stroll", races:406, wins:32, poles:22, best:"世界冠军×2", rank2025:"第8" },
  { name:"Lance Stroll", nat:"加拿大", age:27, num:18, team:"Aston Martin", teammate:"Fernando Alonso", races:172, wins:0, poles:0, best:"第3名", rank2025:"第14" },
  { name:"Pierre Gasly", nat:"法国", age:30, num:10, team:"Alpine", teammate:"Franco Colapinto", races:164, wins:1, poles:0, best:"第1名", rank2025:"第9" },
  { name:"Franco Colapinto", nat:"阿根廷", age:23, num:43, team:"Alpine", teammate:"Pierre Gasly", races:18, wins:0, poles:0, best:"第8名", rank2025:"第19" },
  { name:"Carlos Sainz", nat:"西班牙", age:31, num:55, team:"Williams", teammate:"Alex Albon", races:224, wins:4, poles:6, best:"第5名", rank2025:"第7" },
  { name:"Alex Albon", nat:"泰国", age:30, num:23, team:"Williams", teammate:"Carlos Sainz", races:104, wins:0, poles:0, best:"第3名", rank2025:"第11" },
  { name:"Nico Hulkenberg", nat:"德国", age:38, num:27, team:"Audi F1 Team", teammate:"Gabriel Bortoleto", races:227, wins:0, poles:1, best:"第4名", rank2025:"第10" },
  { name:"Gabriel Bortoleto", nat:"巴西", age:21, num:5, team:"Audi F1 Team", teammate:"Nico Hulkenberg", races:9, wins:0, poles:0, best:"新秀", rank2025:"F3冠军" },
  { name:"Esteban Ocon", nat:"法国", age:29, num:31, team:"Toyota GR Haas", teammate:"Oliver Bearman", races:164, wins:1, poles:0, best:"第1名", rank2025:"第15" },
  { name:"Oliver Bearman", nat:"英国", age:21, num:87, team:"Toyota GR Haas", teammate:"Esteban Ocon", races:9, wins:0, poles:0, best:"新秀", rank2025:"F2第5" },
  { name:"Sergio Perez", nat:"墨西哥", age:36, num:11, team:"Cadillac Racing", teammate:"Valtteri Bottas", races:281, wins:6, poles:3, best:"第2名", rank2025:"第16" },
  { name:"Valtteri Bottas", nat:"芬兰", age:36, num:77, team:"Cadillac Racing", teammate:"Sergio Perez", races:247, wins:10, poles:20, best:"第2名", rank2025:"第18" },
  { name:"Liam Lawson", nat:"新西兰", age:24, num:30, team:"Racing Bulls", teammate:"Arvid Lindblad", races:31, wins:0, poles:0, best:"第9名", rank2025:"第10" }
];

// ===== champions =====
const champions = [
  [1950,"Giuseppe Farina","Alfa Romeo"],[1951,"Juan Manuel Fangio","Alfa Romeo"],
  [1952,"Alberto Ascari","Ferrari"],[1953,"Alberto Ascari","Ferrari"],
  [1954,"Juan Manuel Fangio","Maserati"],[1955,"Juan Manuel Fangio","Mercedes"],
  [1956,"Juan Manuel Fangio","Ferrari"],[1957,"Juan Manuel Fangio","Maserati"],
  [1958,"Mike Hawthorn","Ferrari"],[1959,"Jack Brabham","Cooper"],
  [1960,"Jack Brabham","Cooper"],[1961,"Phil Hill","Ferrari"],
  [1962,"Graham Hill","BRM"],[1963,"Jim Clark","Lotus"],
  [1964,"John Surtees","Ferrari"],[1965,"Jim Clark","Lotus"],
  [1966,"Jack Brabham","Brabham"],[1967,"Denny Hulme","Brabham"],
  [1968,"Graham Hill","Lotus"],[1969,"Jackie Stewart","Matra"],
  [1970,"Jochen Rindt","Lotus"],[1971,"Jackie Stewart","Tyrrell"],
  [1972,"Emerson Fittipaldi","Lotus"],[1973,"Jackie Stewart","Tyrrell"],
  [1974,"Emerson Fittipaldi","McLaren"],[1975,"Niki Lauda","Ferrari"],
  [1976,"James Hunt","McLaren"],[1977,"Niki Lauda","Ferrari"],
  [1978,"Mario Andretti","Lotus"],[1979,"Jody Scheckter","Ferrari"],
  [1980,"Alan Jones","Williams"],[1981,"Nelson Piquet","Brabham"],
  [1982,"Keke Rosberg","Williams"],[1983,"Nelson Piquet","Brabham"],
  [1984,"Niki Lauda","McLaren"],[1985,"Alain Prost","McLaren"],
  [1986,"Alain Prost","McLaren"],[1987,"Nelson Piquet","Williams"],
  [1988,"Ayrton Senna","McLaren"],[1989,"Alain Prost","McLaren"],
  [1990,"Ayrton Senna","McLaren"],[1991,"Ayrton Senna","McLaren"],
  [1992,"Nigel Mansell","Williams"],[1993,"Alain Prost","Williams"],
  [1994,"Michael Schumacher","Benetton"],[1995,"Michael Schumacher","Benetton"],
  [1996,"Damon Hill","Williams"],[1997,"Jacques Villeneuve","Williams"],
  [1998,"Mika Hakkinen","McLaren"],[1999,"Mika Hakkinen","McLaren"],
  [2000,"Michael Schumacher","Ferrari"],[2001,"Michael Schumacher","Ferrari"],
  [2002,"Michael Schumacher","Ferrari"],[2003,"Michael Schumacher","Ferrari"],
  [2004,"Michael Schumacher","Ferrari"],[2005,"Fernando Alonso","Renault"],
  [2006,"Fernando Alonso","Renault"],[2007,"Kimi Raikkonen","Ferrari"],
  [2008,"Lewis Hamilton","McLaren"],[2009,"Jenson Button","Brawn"],
  [2010,"Sebastian Vettel","Red Bull"],[2011,"Sebastian Vettel","Red Bull"],
  [2012,"Sebastian Vettel","Red Bull"],[2013,"Sebastian Vettel","Red Bull"],
  [2014,"Lewis Hamilton","Mercedes"],[2015,"Lewis Hamilton","Mercedes"],
  [2016,"Nico Rosberg","Mercedes"],[2017,"Lewis Hamilton","Mercedes"],
  [2018,"Lewis Hamilton","Mercedes"],[2019,"Lewis Hamilton","Mercedes"],
  [2020,"Lewis Hamilton","Mercedes"],[2021,"Max Verstappen","Red Bull"],
  [2022,"Max Verstappen","Red Bull"],[2023,"Max Verstappen","Red Bull"],
  [2024,"Max Verstappen","Red Bull"],[2025,"Lando Norris","McLaren"]
];

// ===== constructorsData =====
const constructorsData = [
  { rank:1, name:"Mercedes", points:333, color:"#27f4d2", drivers2026:["Russell","Antonelli"], change:0 },
  { rank:2, name:"Ferrari", points:255, color:"#dc0000", drivers2026:["Leclerc","Hamilton"], change:0 },
  { rank:3, name:"McLaren", points:179, color:"#ff8000", drivers2026:["Norris","Piastri"], change:0 },
  { rank:4, name:"Red Bull", points:128, color:"#1e41b0", drivers2026:["Verstappen","Hadjar"], change:0 },
  { rank:5, name:"Alpine", points:60, color:"#0093cc", drivers2026:["Gasly","Colapinto"], change:0 },
  { rank:6, name:"Racing Bulls", points:59, color:"#6699ff", drivers2026:["Lawson","Lindblad"], change:0 },
  { rank:7, name:"Haas", points:21, color:"#cc0000", drivers2026:["Bearman","Ocon"], change:0 },
  { rank:8, name:"Williams", points:11, color:"#005aff", drivers2026:["Sainz","Albon"], change:0 },
  { rank:9, name:"Audi", points:6, color:"#c0c0c0", drivers2026:["Hulkenberg","Bortoleto"], change:0 },
  { rank:10, name:"Aston Martin", points:1, color:"#006f62", drivers2026:["Alonso","Stroll"], change:0 },
  { rank:11, name:"Cadillac", points:0, color:"#cf9f3f", drivers2026:["Perez","Bottas"], note:"2026新队", change:0 }
];

// ===== driverStandings =====
const driverStandings = [
  { rank:1, name:"Antonelli", team:"Mercedes", pts:179, color:"#27f4d2", behind:0 },
  { rank:2, name:"Russell", team:"Mercedes", pts:154, color:"#27f4d2", behind:25 },
  { rank:3, name:"Hamilton", team:"Ferrari", pts:147, color:"#dc0000", behind:32 },
  { rank:4, name:"Leclerc", team:"Ferrari", pts:108, color:"#dc0000", behind:71 },
  { rank:5, name:"Norris", team:"McLaren", pts:97, color:"#ff8000", behind:82 },
  { rank:6, name:"Piastri", team:"McLaren", pts:82, color:"#ff8000", behind:97 },
  { rank:7, name:"Verstappen", team:"Red Bull", pts:76, color:"#1e41b0", behind:103 },
  { rank:8, name:"Hadjar", team:"Red Bull", pts:52, color:"#1e41b0", behind:127 },
  { rank:9, name:"Gasly", team:"Alpine", pts:42, color:"#0093cc", behind:137 },
  { rank:10, name:"Lawson", team:"Racing Bulls", pts:39, color:"#6699ff", behind:140 },
  { rank:11, name:"Lindblad", team:"Racing Bulls", pts:20, color:"#6699ff", behind:159 },
  { rank:12, name:"Bearman", team:"Haas", pts:18, color:"#cc0000", behind:161 },
  { rank:13, name:"Colapinto", team:"Alpine", pts:18, color:"#0093cc", behind:161 },
  { rank:14, name:"Bortoleto", team:"Audi", pts:6, color:"#c0c0c0", behind:173 },
  { rank:15, name:"Sainz", team:"Williams", pts:6, color:"#005aff", behind:173 },
  { rank:16, name:"Albon", team:"Williams", pts:5, color:"#005aff", behind:174 },
  { rank:17, name:"Ocon", team:"Haas", pts:3, color:"#cc0000", behind:176 },
  { rank:18, name:"Alonso", team:"Aston Martin", pts:1, color:"#006f62", behind:178 },
  { rank:19, name:"Hulkenberg", team:"Audi", pts:0, color:"#c0c0c0", behind:179 },
  { rank:20, name:"Bottas", team:"Cadillac", pts:0, color:"#cf9f3f", behind:179 },
  { rank:21, name:"Perez", team:"Cadillac", pts:0, color:"#cf9f3f", behind:179 },
  { rank:22, name:"Stroll", team:"Aston Martin", pts:0, color:"#006f62", behind:179 }
];

// ===== raceResults =====
const raceResults = [
  {
    gp:"澳大利亚大奖赛", circuit:"Albert Park", country:"🇦🇺 澳大利亚", dates:"3.6-8", flag:"🇦🇺",
    podium: [{pos:1,name:"Russell",team:"Mercedes"},{pos:2,name:"Antonelli",team:"Mercedes"},{pos:3,name:"Leclerc",team:"Ferrari"}],
    fastest:"Russell", dnfs:"无重大退赛",
    table: [
      {pos:1,name:"Russell",team:"Mercedes",time:"1:23:06.801"},
      {pos:2,name:"Antonelli",team:"Mercedes",time:"+2.974s"},
      {pos:3,name:"Leclerc",team:"Ferrari",time:"+15.519s"},
      {pos:4,name:"Hamilton",team:"Ferrari",time:"+16.144s"},
      {pos:5,name:"Norris",team:"McLaren",time:"+51.741s"},
      {pos:6,name:"Verstappen",team:"Red Bull",time:"+54.617s"},
      {pos:7,name:"Bearman",team:"Haas",time:"+1 lap"},
      {pos:8,name:"Lindblad",team:"Racing Bulls",time:"+1 lap"},
      {pos:9,name:"Bortoleto",team:"Audi",time:"+1 lap"},
      {pos:10,name:"Gasly",team:"Alpine",time:"+1 lap"}
    ]
  },
  {
    gp:"中国大奖赛", circuit:"上海国际赛车场", country:"🇨🇳 中国", dates:"3.13-15", flag:"🇨🇳",
    podium: [{pos:1,name:"Antonelli",team:"Mercedes"},{pos:2,name:"Russell",team:"Mercedes"},{pos:3,name:"Hamilton",team:"Ferrari"}],
    fastest:"Antonelli", dnfs:"Verstappen, Alonso, Stroll — DNF; Piastri, Norris, Bortoleto, Albon — DNS",
    table: [
      {pos:1,name:"Antonelli",team:"Mercedes",time:"1:33:15.607"},
      {pos:2,name:"Russell",team:"Mercedes",time:"+5.515s"},
      {pos:3,name:"Hamilton",team:"Ferrari",time:"+25.267s"},
      {pos:4,name:"Leclerc",team:"Ferrari",time:"+28.894s"},
      {pos:5,name:"Bearman",team:"Haas",time:"+57.268s"},
      {pos:6,name:"Gasly",team:"Alpine",time:"+59.647s"},
      {pos:7,name:"Lawson",team:"Racing Bulls",time:"+80.588s"},
      {pos:8,name:"Hadjar",team:"Red Bull",time:"+87.247s"},
      {pos:9,name:"Sainz",team:"Williams",time:"+1 lap"},
      {pos:10,name:"Colapinto",team:"Alpine",time:"+1 lap"}
    ]
  },
  {
    gp:"日本大奖赛", circuit:"铃鹿", country:"🇯🇵 日本", dates:"3.27-29", flag:"🇯🇵",
    podium: [{pos:1,name:"Antonelli",team:"Mercedes"},{pos:2,name:"Piastri",team:"McLaren"},{pos:3,name:"Leclerc",team:"Ferrari"}],
    fastest:"Antonelli", dnfs:"Stroll, Bearman — DNF",
    table: [
      {pos:1,name:"Antonelli",team:"Mercedes",time:"1:28:03.403"},
      {pos:2,name:"Piastri",team:"McLaren",time:"+13.722s"},
      {pos:3,name:"Leclerc",team:"Ferrari",time:"+15.270s"},
      {pos:4,name:"Russell",team:"Mercedes",time:"+15.754s"},
      {pos:5,name:"Norris",team:"McLaren",time:"+23.479s"},
      {pos:6,name:"Hamilton",team:"Ferrari",time:"+25.037s"},
      {pos:7,name:"Gasly",team:"Alpine",time:"+32.340s"},
      {pos:8,name:"Verstappen",team:"Red Bull",time:"+32.677s"},
      {pos:9,name:"Lawson",team:"Racing Bulls",time:"+50.180s"},
      {pos:10,name:"Ocon",team:"Haas",time:"+51.216s"}
    ]
  },
  {
    gp:"迈阿密大奖赛", circuit:"Miami International Autodrome", country:"🇺🇸 美国", dates:"5.1-3", flag:"🇺🇸",
    podium: [{pos:1,name:"Antonelli",team:"Mercedes"},{pos:2,name:"Norris",team:"McLaren"},{pos:3,name:"Piastri",team:"McLaren"}],
    fastest:"Norris", dnfs:"Hülkenberg, Lawson, Gasly, Hadjar — DNF",
    table: [
      {pos:1,name:"Antonelli",team:"Mercedes",time:"1:33:19.273"},
      {pos:2,name:"Norris",team:"McLaren",time:"+3.264s"},
      {pos:3,name:"Piastri",team:"McLaren",time:"+27.092s"},
      {pos:4,name:"Russell",team:"Mercedes",time:"+43.051s"},
      {pos:5,name:"Verstappen",team:"Red Bull",time:"+48.949s"},
      {pos:6,name:"Hamilton",team:"Ferrari",time:"+53.753s"},
      {pos:7,name:"Colapinto",team:"Alpine",time:"+61.871s"},
      {pos:8,name:"Leclerc",team:"Ferrari",time:"+64.245s"},
      {pos:9,name:"Sainz",team:"Williams",time:"+82.072s"},
      {pos:10,name:"Albon",team:"Williams",time:"+90.972s"}
    ]
  },
  {
    gp:"加拿大大奖赛", circuit:"Circuit Gilles Villeneuve", country:"🇨🇦 加拿大", dates:"5.22-24", flag:"🇨🇦",
    podium: [{pos:1,name:"Antonelli",team:"Mercedes"},{pos:2,name:"Hamilton",team:"Ferrari"},{pos:3,name:"Verstappen",team:"Red Bull"}],
    fastest:"Antonelli", dnfs:"Pérez, Norris, Russell, Alonso, Albon — DNF; Lindblad — DNS",
    table: [
      {pos:1,name:"Antonelli",team:"Mercedes",time:"1:28:15.758"},
      {pos:2,name:"Hamilton",team:"Ferrari",time:"+10.768s"},
      {pos:3,name:"Verstappen",team:"Red Bull",time:"+11.276s"},
      {pos:4,name:"Leclerc",team:"Ferrari",time:"+44.151s"},
      {pos:5,name:"Hadjar",team:"Red Bull",time:"+1 lap"},
      {pos:6,name:"Colapinto",team:"Alpine",time:"+1 lap"},
      {pos:7,name:"Lawson",team:"Racing Bulls",time:"+1 lap"},
      {pos:8,name:"Gasly",team:"Alpine",time:"+1 lap"},
      {pos:9,name:"Sainz",team:"Williams",time:"+1 lap"},
      {pos:10,name:"Bearman",team:"Haas",time:"+1 lap"}
    ]
  },
  {
    gp:"摩纳哥大奖赛", circuit:"Circuit de Monaco", country:"🇲🇨 摩纳哥", dates:"6.5-7", flag:"🇲🇨",
    podium: [{pos:1,name:"Antonelli",team:"Mercedes"},{pos:2,name:"Hamilton",team:"Ferrari"},{pos:3,name:"Leclerc",team:"Ferrari"}],
    fastest:"Antonelli", dnfs:"Stroll — DNF",
    table: [
      {pos:1,name:"Antonelli",team:"Mercedes",time:"2:23:31.243"},
      {pos:2,name:"Hamilton",team:"Ferrari",time:"+3.189s"},
      {pos:3,name:"Leclerc",team:"Ferrari",time:"+6.147s"},
      {pos:4,name:"Russell",team:"Mercedes",time:"+10.524s"},
      {pos:5,name:"Piastri",team:"McLaren",time:"+14.387s"},
      {pos:6,name:"Norris",team:"McLaren",time:"+19.102s"},
      {pos:7,name:"Verstappen",team:"Red Bull",time:"+25.846s"},
      {pos:8,name:"Gasly",team:"Alpine",time:"+1 lap"},
      {pos:9,name:"Lawson",team:"Racing Bulls",time:"+1 lap"},
      {pos:10,name:"Colapinto",team:"Alpine",time:"+1 lap"}
    ]
  },
  {
    gp:"英国大奖赛", circuit:"Silverstone", country:"🇬🇧 英国", dates:"7.3-5", flag:"🇬🇧",
    podium: [{pos:1,name:"Leclerc",team:"Ferrari"},{pos:2,name:"Russell",team:"Mercedes"},{pos:3,name:"Hamilton",team:"Ferrari"}],
    fastest:"Antonelli", dnfs:"Verstappen(撞车), Albon, Hülkenberg — DNF",
    table: [
      {pos:1,name:"Leclerc",team:"Ferrari",time:"1:27:11.335"},
      {pos:2,name:"Russell",team:"Mercedes",time:"+0.427s"},
      {pos:3,name:"Hamilton",team:"Ferrari",time:"+0.772s"},
      {pos:4,name:"Norris",team:"McLaren",time:"+1.149s"},
      {pos:5,name:"Hadjar",team:"Red Bull",time:"+1.598s"},
      {pos:6,name:"Lawson",team:"Racing Bulls",time:"+2.023s"},
      {pos:7,name:"Lindblad",team:"Racing Bulls",time:"+2.214s"},
      {pos:8,name:"Bortoleto",team:"Audi",time:"+2.413s"},
      {pos:9,name:"Colapinto",team:"Alpine",time:"+3.229s"},
      {pos:10,name:"Gasly",team:"Alpine",time:"+3.445s"}
    ]
  }
];

// ===== trackDetailData =====
const trackDetailData = [
  { id:"albert-park", name:"Albert Park", gp:"澳大利亚大奖赛", country:"🇦🇺 澳大利亚", firstRace:1996,
    laps:58, length:"5.278 km", dist:"306.124 km", corners:14, drs:4,
    record:{driver:"Leclerc", time:"1:19.813", year:2024},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Australia_Circuit" alt="Australia Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"shanghai", name:"上海国际赛车场", gp:"中国大奖赛", country:"🇨🇳 中国", firstRace:2004,
    laps:56, length:"5.451 km", dist:"305.256 km", corners:16, drs:3,
    record:{driver:"Schumacher", time:"1:32.238", year:2004},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/China_Circuit" alt="China Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"suzuka", name:"铃鹿", gp:"日本大奖赛", country:"🇯🇵 日本", firstRace:1987,
    laps:53, length:"5.807 km", dist:"307.771 km", corners:18, drs:2,
    record:{driver:"Hamilton", time:"1:30.983", year:2019},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Japan_Circuit" alt="Japan Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"bahrain", name:"Bahrain International Circuit", gp:"巴林大奖赛", country:"🇧🇭 巴林", firstRace:2004,
    laps:57, length:"5.412 km", dist:"308.484 km", corners:15, drs:3,
    record:{driver:"De la Rosa", time:"1:31.447", year:2005},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Bahrain_Circuit" alt="Bahrain Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"jeddah", name:"Jeddah Corniche Circuit", gp:"沙特阿拉伯大奖赛", country:"🇸🇦 沙特阿拉伯", firstRace:2021,
    laps:50, length:"6.174 km", dist:"308.700 km", corners:27, drs:3,
    record:{driver:"Hamilton", time:"1:30.734", year:2021},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Saudi_Arabia_Circuit" alt="Saudi_Arabia Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"miami", name:"Miami International Autodrome", gp:"迈阿密大奖赛", country:"🇺🇸 美国", firstRace:2022,
    laps:57, length:"5.412 km", dist:"308.326 km", corners:19, drs:3,
    record:{driver:"Verstappen", time:"1:29.708", year:2023},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Miami_Circuit" alt="Miami Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"montreal", name:"Circuit Gilles Villeneuve", gp:"加拿大大奖赛", country:"🇨🇦 加拿大", firstRace:1978,
    laps:68, length:"4.361 km", dist:"296.548 km", corners:14, drs:3,
    record:{driver:"Bottas", time:"1:13.078", year:2019},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Canada_Circuit" alt="Canada Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"monaco", name:"Circuit de Monaco", gp:"摩纳哥大奖赛", country:"🇲🇨 摩纳哥", firstRace:1950,
    laps:78, length:"3.337 km", dist:"260.286 km", corners:19, drs:1,
    record:{driver:"Hamilton", time:"1:12.909", year:2021},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Monaco_Circuit" alt="Monaco Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"barcelona", name:"Circuit de Barcelona-Catalunya", gp:"西班牙大奖赛(巴塞罗那)", country:"🇪🇸 西班牙", firstRace:1991,
    laps:66, length:"4.657 km", dist:"307.362 km", corners:16, drs:2,
    record:{driver:"Verstappen", time:"1:16.330", year:2023},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Spain_Circuit" alt="Spain Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"red-bull-ring", name:"Red Bull Ring", gp:"奥地利大奖赛", country:"🇦🇹 奥地利", firstRace:1970,
    laps:71, length:"4.318 km", dist:"306.578 km", corners:10, drs:3,
    record:{driver:"Sainz", time:"1:05.619", year:2020},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Austria_Circuit" alt="Austria Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"silverstone", name:"Silverstone", gp:"英国大奖赛", country:"🇬🇧 英国", firstRace:1950,
    laps:52, length:"5.891 km", dist:"306.332 km", corners:18, drs:2,
    record:{driver:"Hamilton", time:"1:27.097", year:2020},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Great_Britain_Circuit" alt="Great_Britain Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"spa", name:"Spa-Francorchamps", gp:"比利时大奖赛", country:"🇧🇪 比利时", firstRace:1950,
    laps:44, length:"7.004 km", dist:"308.176 km", corners:19, drs:2,
    record:{driver:"Bottas", time:"1:46.286", year:2018},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Belgium_Circuit" alt="Belgium Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"hungaroring", name:"Hungaroring", gp:"匈牙利大奖赛", country:"🇭🇺 匈牙利", firstRace:1986,
    laps:70, length:"4.381 km", dist:"306.670 km", corners:14, drs:2,
    record:{driver:"Hamilton", time:"1:16.627", year:2020},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Hungary_Circuit" alt="Hungary Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"zandvoort", name:"Zandvoort", gp:"荷兰大奖赛", country:"🇳🇱 荷兰", firstRace:1952,
    laps:72, length:"4.259 km", dist:"306.648 km", corners:14, drs:2,
    record:{driver:"Hamilton", time:"1:11.097", year:2021},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Netherlands_Circuit" alt="Netherlands Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"monza", name:"Monza", gp:"意大利大奖赛", country:"🇮🇹 意大利", firstRace:1950,
    laps:53, length:"5.793 km", dist:"307.029 km", corners:11, drs:2,
    record:{driver:"Barrichello", time:"1:21.046", year:2004},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Italy_Circuit" alt="Italy Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"madrid", name:"Madrid Street Circuit", gp:"马德里大奖赛", country:"🇪🇸 西班牙", firstRace:2026,
    laps:65, length:"5.474 km", dist:"355.810 km", corners:20, drs:2,
    record:{driver:"—", time:"—", year:"2026 新赛道"},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Madrid_Circuit" alt="Madrid Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"baku", name:"Baku City Circuit", gp:"阿塞拜疆大奖赛", country:"🇦🇿 阿塞拜疆", firstRace:2016,
    laps:51, length:"6.003 km", dist:"306.153 km", corners:20, drs:2,
    record:{driver:"Leclerc", time:"1:43.009", year:2019},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Azerbaijan_Circuit" alt="Azerbaijan Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"singapore", name:"Marina Bay", gp:"新加坡大奖赛", country:"🇸🇬 新加坡", firstRace:2008,
    laps:61, length:"5.063 km", dist:"308.843 km", corners:23, drs:3,
    record:{driver:"Hamilton", time:"1:36.015", year:2018},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Singapore_Circuit" alt="Singapore Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"cota", name:"COTA", gp:"美国大奖赛(奥斯汀)", country:"🇺🇸 美国", firstRace:2012,
    laps:56, length:"5.513 km", dist:"308.728 km", corners:20, drs:2,
    record:{driver:"Leclerc", time:"1:36.169", year:2019},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/USA_Circuit" alt="USA Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"mexico", name:"Autodromo Hermanos Rodriguez", gp:"墨西哥大奖赛", country:"🇲🇽 墨西哥", firstRace:1963,
    laps:71, length:"4.304 km", dist:"305.584 km", corners:17, drs:3,
    record:{driver:"Bottas", time:"1:17.774", year:2021},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Mexico_Circuit" alt="Mexico Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"interlagos", name:"Interlagos", gp:"巴西大奖赛", country:"🇧🇷 巴西", firstRace:1973,
    laps:71, length:"4.309 km", dist:"305.939 km", corners:15, drs:2,
    record:{driver:"Bottas", time:"1:10.540", year:2018},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Brazil_Circuit" alt="Brazil Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"las-vegas", name:"Las Vegas Strip Circuit", gp:"拉斯维加斯大奖赛", country:"🇺🇸 美国", firstRace:2023,
    laps:50, length:"6.201 km", dist:"310.050 km", corners:17, drs:2,
    record:{driver:"Piastri", time:"1:34.876", year:2024},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Las_Vegas_Circuit" alt="Las_Vegas Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"lusail", name:"Lusail International Circuit", gp:"卡塔尔大奖赛", country:"🇶🇦 卡塔尔", firstRace:2021,
    laps:57, length:"5.419 km", dist:"308.883 km", corners:16, drs:2,
    record:{driver:"Verstappen", time:"1:24.319", year:2023},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Qatar_Circuit" alt="Qatar Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  },
  { id:"yas-marina", name:"Yas Marina", gp:"阿布扎比大奖赛", country:"🇦🇪 阿联酋", firstRace:2009,
    laps:58, length:"5.281 km", dist:"306.298 km", corners:21, drs:2,
    record:{driver:"Verstappen", time:"1:26.103", year:2021},
    layout:'<img src="https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Abu_Dhabi_Circuit" alt="Abu_Dhabi Circuit Map" loading="lazy" onerror=\"this.style.display=\'none\'\">'
  }
];

// ===== driverData =====
const driverData = [
  { name:"Kimi Antonelli", team:"Mercedes", nationality:"Italy", flag:"🇮🇹", number:"12", dob:"2006-08-25", age:19, races:9, wins:5, podiums:5, poles:1, fastestLaps:3, championships:0, bio:"2026赛季F1新人王，梅赛德斯青训出品。首秀即夺冠，以惊人的速度和成熟的比赛智商震惊围场，被视作未来十年最有潜力的车手。" },
  { name:"George Russell", team:"Mercedes", nationality:"United Kingdom", flag:"🇬🇧", number:"63", dob:"1998-02-15", age:28, races:148, wins:4, podiums:21, poles:5, fastestLaps:8, championships:0, bio:"梅赛德斯领军车手，以精准的排位赛表现和稳定的长距离节奏著称。2026赛季与新人Antonelli搭档，展现成熟领袖风范。" },
  { name:"Charles Leclerc", team:"Ferrari", nationality:"Monaco", flag:"🇲🇨", number:"16", dob:"1997-10-16", age:28, races:170, wins:9, podiums:44, poles:26, fastestLaps:10, championships:0, bio:"法拉利王牌，排位赛之王。单圈速度围场顶尖，但需要更稳定的正赛发挥来争夺世界冠军。2026赛季搭档Hamilton组成梦幻阵容。" },
  { name:"Lewis Hamilton", team:"Ferrari", nationality:"United Kingdom", flag:"🇬🇧", number:"44", dob:"1985-01-07", age:41, races:362, wins:105, podiums:203, poles:104, fastestLaps:67, championships:7, bio:"七届世界冠军，F1历史最伟大车手之一。2025年加盟法拉利，追逐第八座世界冠军的梦想。2026赛季适应新规后迅速展现竞争力。" },
  { name:"Lando Norris", team:"McLaren", nationality:"United Kingdom", flag:"🇬🇧", number:"4", dob:"1999-11-13", age:26, races:148, wins:10, podiums:35, poles:10, fastestLaps:8, championships:1, bio:"2025赛季世界冠军！迈凯伦青训的杰出代表，以敏捷的速度和风趣的性格成为车迷最爱。2026赛季目标是卫冕。" },
  { name:"Oscar Piastri", team:"McLaren", nationality:"Australia", flag:"🇦🇺", number:"81", dob:"2001-04-06", age:25, races:72, wins:4, podiums:17, poles:0, fastestLaps:3, championships:0, bio:"冷静沉稳的澳大利亚新星，F2和F3连续冠军出身。正赛节奏和轮胎管理能力突出，被广泛看好在未来挑战世界冠军。" },
  { name:"Max Verstappen", team:"Red Bull Racing", nationality:"Netherlands", flag:"🇳🇱", number:"1", dob:"1997-09-30", age:28, races:224, wins:63, podiums:112, poles:40, fastestLaps:33, championships:4, bio:"四届世界冠军，以无与伦比的赛车本能和极限攻防著称。2026赛季面临新规挑战，但仍是任何赛道上不可忽视的力量。" },
  { name:"Isack Hadjar", team:"Red Bull Racing", nationality:"France", flag:"🇫🇷", number:"6", dob:"2004-09-28", age:21, races:9, wins:0, podiums:0, poles:0, fastestLaps:0, championships:0, bio:"红牛青训出品，2025年F2亚军。2026年以新人身份升入大红牛，在Verstappen身边学习是巨大的机会和挑战。" },
  { name:"Pierre Gasly", team:"Alpine", nationality:"France", flag:"🇫🇷", number:"10", dob:"1996-02-07", age:30, races:164, wins:1, podiums:5, poles:0, fastestLaps:3, championships:0, bio:"Alpine的法国本土英雄，2020年意大利大奖赛胜者。稳定的积分收割机，在2026赛季带领车队转投梅赛德斯动力单元。" },
  { name:"Franco Colapinto", team:"Alpine", nationality:"Argentina", flag:"🇦🇷", number:"43", dob:"2003-05-27", age:23, races:18, wins:0, podiums:0, poles:0, fastestLaps:0, championships:0, bio:"阿根廷新星，2024年威廉姆斯赛季中途登场即展现不俗速度。2026年转会Alpine开启全新篇章，南美车迷的新希望。" },
  { name:"Liam Lawson", team:"Racing Bulls", nationality:"New Zealand", flag:"🇳🇿", number:"30", dob:"2002-02-11", age:24, races:31, wins:0, podiums:0, poles:0, fastestLaps:0, championships:0, bio:"新西兰斗士，红牛青训体系最强产品之一。以激进的超车风格和永不放弃的比赛态度赢得围场尊重，2026赛季继续在Racing Bulls证明自己。" },
  { name:"Arvid Lindblad", team:"Racing Bulls", nationality:"United Kingdom", flag:"🇬🇧", number:"7", dob:"2007-08-08", age:18, races:9, wins:0, podiums:0, poles:0, fastestLaps:0, championships:0, bio:"F1历史上最年轻的车手之一，红牛青训新一代领军人物。2025年F3冠军直跳F1，天赋惊人但需要时间积累经验。" },
  { name:"Esteban Ocon", team:"Haas", nationality:"France", flag:"🇫🇷", number:"31", dob:"1996-09-17", age:29, races:164, wins:1, podiums:3, poles:0, fastestLaps:0, championships:0, bio:"坚韧的法国车手，2021年匈牙利大奖赛胜者。转会Haas后担任队内领袖角色，搭档新人Bearman开启车队新纪元。" },
  { name:"Oliver Bearman", team:"Haas", nationality:"United Kingdom", flag:"🇬🇧", number:"87", dob:"2005-05-08", age:21, races:9, wins:0, podiums:0, poles:0, fastestLaps:0, championships:0, bio:"法拉利青训培养的英国新星，2024年沙特站代打法拉利即拿分。2026年正式升入Haas，展现出超越年龄的比赛智慧。" },
  { name:"Carlos Sainz", team:"Williams", nationality:"Spain", flag:"🇪🇸", number:"55", dob:"1994-09-01", age:31, races:224, wins:4, podiums:27, poles:6, fastestLaps:4, championships:0, bio:"经验丰富的西班牙车手，多站分站冠军。转会Williams后承担重建重任，搭档Albon组成最具战斗力的中游阵容。" },
  { name:"Alexander Albon", team:"Williams", nationality:"Thailand", flag:"🇹🇭", number:"23", dob:"1996-03-23", age:30, races:116, wins:0, podiums:2, poles:0, fastestLaps:0, championships:0, bio:"泰国骄傲，威廉姆斯复兴的关键人物。2026赛季有了更快的赛车和更强的队友，目标直指中游前列。" },
  { name:"Nico Hülkenberg", team:"Audi", nationality:"Germany", flag:"🇩🇪", number:"27", dob:"1987-08-19", age:38, races:235, wins:0, podiums:0, poles:1, fastestLaps:2, championships:0, bio:"德国老将，F1无冕之王之一。以排位赛的惊人单圈能力和丰富的赛车经验著称，作为Audi工厂车队元年车手肩负重任。" },
  { name:"Gabriel Bortoleto", team:"Audi", nationality:"Brazil", flag:"🇧🇷", number:"5", dob:"2004-10-14", age:21, races:9, wins:0, podiums:0, poles:0, fastestLaps:0, championships:0, bio:"巴西新星，2024年F3冠军、2025年F2冠军。两连跳天赋惊人，在Audi工厂车队元年获得宝贵F1席位。" },
  { name:"Sergio Pérez", team:"Cadillac", nationality:"Mexico", flag:"🇲🇽", number:"11", dob:"1990-01-26", age:36, races:289, wins:6, podiums:39, poles:1, fastestLaps:12, championships:0, bio:"墨西哥传奇，轮胎管理大师。在红牛效力多年后转投全新Cadillac F1车队，用丰富经验帮助美国新军站稳脚跟。" },
  { name:"Valtteri Bottas", team:"Cadillac", nationality:"Finland", flag:"🇫🇮", number:"77", dob:"1989-08-28", age:36, races:247, wins:10, podiums:67, poles:20, fastestLaps:19, championships:0, bio:"芬兰冰人，10次分站冠军得主。在梅赛德斯时期是Hamilton最强副手，2026赛季与Pérez搭档为Cadillac注入丰富经验。" },
  { name:"Fernando Alonso", team:"Aston Martin", nationality:"Spain", flag:"🇪🇸", number:"14", dob:"1981-07-29", age:44, races:406, wins:32, podiums:106, poles:22, fastestLaps:28, championships:2, bio:"两届世界冠军，F1活化石。44岁仍保持顶级竞争力，赛车智慧无与伦比。2026赛季搭档本田动力单元和Newey设计的AMR26追逐第三冠。" },
  { name:"Lance Stroll", team:"Aston Martin", nationality:"Canada", flag:"🇨🇦", number:"18", dob:"1998-10-29", age:27, races:172, wins:0, podiums:3, poles:1, fastestLaps:0, championships:0, bio:"加拿大人，阿隆索的长期队友。在2026新规下拥有Newey设计的赛车，这是证明自己的绝佳机会。" },
];

