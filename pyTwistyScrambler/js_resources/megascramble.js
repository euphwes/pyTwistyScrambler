var megaScrambler = (function(mega, rn, rndEl) {
	var cubesuff=["","2","'"];
	var minxsuff=["","2","'","2'"];
	var args = {
		"111": [[["x"],["y"],["z"]],cubesuff], // 1x1x1
		"2223": [[["U"],["R"],["F"]],cubesuff], // 2x2x2 (3-gen)
		"2226": [[[["U","D"]],[["R","L"]],[["F","B"]]],cubesuff], // 2x2x2 (6-gen)
		"333o": [[["U","D"],["R","L"],["F","B"]],cubesuff], // 3x3x3 (old style)
		"334": [[[["U","U'","U2"],["u","u'","u2"]],[["R2","L2","M2"]],[["F2","B2","S2"]]]], // 3x3x4
		"336": [[[["U","U'","U2"],["u","u'","u2"],["3u","3u2","3u'"]],[["R2","L2","M2"]],[["F2","B2","S2"]]]], // 3x3x6
		"888": [[["U","D","u","d","3u","3d","4u"],["R","L","r","l","3r","3l","4r"],["F","B","f","b","3f","3b","4f"]],cubesuff], // 8x8x8 (SiGN)
		"999": [[["U","D","u","d","3u","3d","4u","4d"],["R","L","r","l","3r","3l","4r","4l"],["F","B","f","b","3f","3b","4f","4b"]],cubesuff], // 9x9x9 (SiGN)
		"101010": [[["U","D","u","d","3u","3d","4u","4d","5u"],["R","L","r","l","3r","3l","4r","4l","5r"],["F","B","f","b","3f","3b","4f","4b","5f"]],cubesuff], // 10x10x10 (SiGN)
		"111111": [[["U","D","u","d","3u","3d","4u","4d","5u","5d"],["R","L","r","l","3r","3l","4r","4l","5r","5l"],["F","B","f","b","3f","3b","4f","4b","5f","5b"]],cubesuff], // 11x11x11 (SiGN)
		"444": [[["U","D","u"],["R","L","r"],["F","B","f"]],cubesuff], // 4x4x4 (SiGN)
		"444wca": [[["U","D","Uw"],["R","L","Rw"],["F","B","Fw"]],cubesuff], // 4x4x4 (WCA)
		"555": [[["U","D","u","d"],["R","L","r","l"],["F","B","f","b"]],cubesuff], // 5x5x5 (SiGN)
		"555wca": [[["U","D","Uw","Dw"],["R","L","Rw","Lw"],["F","B","Fw","Bw"]],cubesuff], // 5x5x5 (WCA)
		"666p": [[["U","D","2U","2D","3U"],["R","L","2R","2L","3R"],["F","B","2F","2B","3F"]],cubesuff], // 6x6x6 (prefix)
		"666wca": [[["U","D","Uw","Dw","3Uw"],["R","L","Rw","Lw","3Rw"],["F","B","Fw","Bw","3Fw"]],cubesuff], // 6x6x6 (WCA)
		"666s": [[["U","D","U&sup2;","D&sup2;","U&sup3;"],["R","L","R&sup2;","L&sup2;","R&sup3;"],["F","B","F&sup2;","B&sup2;","F&sup3;"]],cubesuff], // 6x6x6 (suffix)
		"666si": [[["U","D","u","d","3u"],["R","L","r","l","3r"],["F","B","f","b","3f"]],cubesuff], // 6x6x6 (SiGN)
		"777p": [[["U","D","2U","2D","3U","3D"],["R","L","2R","2L","3R","3L"],["F","B","2F","2B","3F","3B"]],cubesuff], // 7x7x7 (prefix)
		"777wca": [[["U","D","Uw","Dw","3Uw","3Dw"],["R","L","Rw","Lw","3Rw","3Lw"],["F","B","Fw","Bw","3Fw","3Bw"]],cubesuff], // 7x7x7 (prefix)
		"777s": [[["U","D","U&sup2;","D&sup2;","U&sup3;","D&sup3;"],["R","L","R&sup2;","L&sup2;","R&sup3;","L&sup3;"],["F","B","F&sup2;","B&sup2;","F&sup3;","B&sup3;"]],cubesuff], // 7x7x7 (suffix)
		"777si": [[["U","D","u","d","3u","3d"],["R","L","r","l","3r","3l"],["F","B","f","b","3f","3b"]],cubesuff], // 7x7x7 (SiGN)
		"cm3": [[[["U<","U>","U2"],["E<","E>","E2"],["D<","D>","D2"]],[["R^","Rv","R2"],["M^","Mv","M2"],["L^","Lv","L2"]]]], // Cmetrick
		"cm2": [[[["U<","U>","U2"],["D<","D>","D2"]],[["R^","Rv","R2"],["L^","Lv","L2"]]]], // Cmetrick Mini
		"233": [[[["U","U'","U2"]],["R2","L2"],["F2","B2"]]], // Domino/2x3x3
		"fto": [[["U","D"],["F","B"],["L","BR"],["R","BL"]],["","'"]], // FTO/Face-Turning Octa
		"gear": [[["U"],["R"],["F"]],["","2","3","4","5","6","'","2'","3'","4'","5'"]],
		"sfl": [[["R","L"],["U","D"]],cubesuff], // Super Floppy Cube
		"ufo": [[["A"],["B"],["C"],[["U","U'","U2'","U2","U3"]]]], // UFO
		"2gen": [[["U"],["R"]],cubesuff], // 2-generator <R,U>
		"2genl": [[["U"],["L"]],cubesuff], // 2-generator <L,U>
		"roux": [[["U"],["M"]],cubesuff], // Roux-generator <M,U>
		"3gen_F": [[["U"],["R"],["F"]],cubesuff], // 3-generator <F,R,U>
		"3gen_L": [[["U"],["R","L"]],cubesuff], // 3-generator <R,U,L>
		"RrU": [[["U"],["R","r"]],cubesuff], // 3-generator <R,r,U>
		"RrUu": [[["U","u"],["R","r"]],cubesuff], // <R,r,U,u>
		"minx2g": [[["U"],["R"]],minxsuff], // megaminx 2-gen
		"mlsll": [[[["R U R'","R U2 R'","R U' R'","R U2' R'"]],[["F' U F","F' U2 F","F' U' F","F' U2' F"]],[["U","U2","U'","U2'"]]]], // megaminx LSLL
		"half": [[["U","D"],["R","L"],["F","B"]],["2"]], // 3x3x3 half turns
		"lsll": [[[["R U R'","R U2 R'","R U' R'"]],[["F' U F","F' U2 F","F' U' F"]],[["U","U2","U'"]]]], // 3x3x3 last slot + last layer (old)
		"prco": [[["F","B"],["U","D"],["L","DBR"],["R","DBL"],["BL","DR"],["BR","DL"]],minxsuff], // Pyraminx Crystal (old style)
		"skb": [[["R"],["L"],["B"],["U"]],["","'"]], // Skewb
		"112": [[["R"],["R"]],cubesuff], // 1x1x2
	}
	
	var args2 = {
		'sia113': '#{[["U","u"],["R","r"]],%c} z2 #{[["U","u"],["R","r"]],%c}',
		'sia123': '#{[["U"],["R","r"]],%c} z2 #{[["U"],["R","r"]],%c}',
		'sia222': '#{[["U"],["R"],["F"]],%c} z2 y #{[["U"],["R"],["F"]],%c}',
		'335': '#{[[["U","U\'","U2"],["D","D\'","D2"]],["R2","L2"],["F2","B2"]]} / ${333}',
		'337': '#{[[["U","U\'","U2","u","u\'","u2","U u","U u\'","U u2","U\' u","U\' u\'","U\' u2","U2 u","U2 u\'","U2 u2"],["D","D\'","D2","d","d\'","d2","D d","D d\'","D d2","D\' d","D\' d\'","D\' d2","D2 d","D2 d\'","D2 d2"]],["R2","L2"],["F2","B2"]]} / ${333}',
		'r234': '2) ${222so}\n3) ${333}\n4) ${[444,40]}',
		'r2345': '${r234}\n5) ${["555",60]}',
		'r23456': '${r2345}\n6) ${["666p",80]}',
		'r234567': '${r23456}\n7) ${["777p",100]}'
	}

	var edges = {
		'4edge': ["r b2",["b2 r'","b2 U2 r U2 r U2 r U2 r"],["u"]],
		'5edge': ["r R b B",["B' b' R' r'","B' b' R' U2 r U2 r U2 r U2 r"],["u","d"]], 
		'6edge': ["3r r 3b b",["3b' b' 3r' r'","3b' b' 3r' U2 r U2 r U2 r U2 r","3b' b' r' U2 3r U2 3r U2 3r U2 3r","3b' b' r2 U2 3r U2 3r U2 3r U2 3r U2 r"],["u","3u","d"]],
		'7edge': ["3r r 3b b",["3b' b' 3r' r'","3b' b' 3r' U2 r U2 r U2 r U2 r","3b' b' r' U2 3r U2 3r U2 3r U2 3r","3b' b' r2 U2 3r U2 3r U2 3r U2 3r U2 r"],["u","3u","3d","d"]]
	}

	function megascramble(type, length) {
		var value = args[type];
		switch (value.length) {
			case 1: return mega(value[0], [""], length);
			case 2: return mega(value[0], value[1], length);
			case 3: return mega(value[0], value[1], value[2]);
		}
	}

	function edgescramble(type, length) {
		var value = edges[type];
		return edge(value[0], value[1], value[2], length);
	}

	function formatScramble(type, length) {
		var value = args2[type].replace(/%l/g, length).replace(/%c/g, '["","2","\'"]');
		var ret = scramble.formatScramble(value,length,true,true);
		return ret;
	}

	/**
	for (var i in args) {
		scramble.reg(i, megascramble);
	}

	for (var i in args2) {
		scramble.reg(i, formatScramble);
	}

	for (var i in edges) {
		scramble.reg(i, edgescramble);
	}
	**/

	function edge(start, end, moves, len) {
		var u=0,d=0,movemis=[];
		var triggers=[["R","R'"],["R'","R"],["L","L'"],["L'","L"],["F'","F"],["F","F'"],["B","B'"],["B'","B"]];
		var ud=["U","D"];
		var scramble = start;
		// initialize move misalignments
		for (var i=0; i<moves.length; i++) {
			movemis[i] = 0;
		}

		for (var i=0; i<len; i++) {
			// apply random moves
			var done = false;
			while (!done) {
				var v = "";
				for (var j=0; j<moves.length; j++) {
					var x = rn(4);
					movemis[j] += x;
					if (x!=0) {
						done = true;
						v += " " + moves[j] + cubesuff[x-1];
					}
				}
			}
			// apply random trigger, update U/D
			var trigger = rn(8);
			var layer = rn(2);
			var turn = rn(3);
			scramble += v + " " + triggers[trigger][0] + " " + ud[layer] + cubesuff[turn] + " " + triggers[trigger][1];
			if (layer==0) {u += turn+1;}
			if (layer==1) {d += turn+1;}
		}

		// fix everything
		for (var i=0; i<moves.length; i++) {
			var x = 4-(movemis[i]%4);
			if (x<4) {
				scramble += " " + moves[i] + cubesuff[x-1];
			}
		}
		u = 4-(u%4); d = 4-(d%4);
		if (u<4) {
			scramble += " U" + cubesuff[u-1];
		}
		if (d<4) {
			scramble += " D" + cubesuff[d-1];
		}
		scramble += " " + rndEl(end);
		return scramble;
	}

	  function get444WCAScramble(n) {
	  	return megascramble("444wca", n);
	  }

  	  function get444SiGNScramble(n) {
	  	return megascramble("444", n);
	  }

	  function get555WCAScramble(n) {
	  	return megascramble("555wca", n);
	  }

  	  function get555SiGNScramble(n) {
	  	return megascramble("555", n);
	  }

	  function get444edgesScramble(n) {
	  	return edgescramble("4edge", n);
	  }

  	  function get555edgesScramble(n) {
	  	return edgescramble("5edge", n);
	  }

  	  function get666WCAScramble(n) {
	  	return megascramble("666wca", n);
	  }

  	  function get666SiGNScramble(n) {
	  	return megascramble("666si", n);
	  }

	  function get666edgesScramble(n) {
	  	return edgescramble("6edge", n);
	  }

	  function get777WCAScramble(n) {
	  	return megascramble("777wca", n);
	  }

  	  function get777SiGNScramble(n) {
	  	return megascramble("777si", n);
	  }

	  function get777edgesScramble(n) {
	  	return edgescramble("7edge", n);
	  }

	  function get333_2genRU_scramble(){
	  	return megascramble("2gen", 25);
	  }

	  function get333_2genLU_scramble(){
	  	return megascramble("2genl", 25);
	  }

	  function get333_2genMU_scramble(){
	  	return megascramble("roux", 25);
	  }

	  function get333_3genFRU_scramble(){
	  	return megascramble("3gen_F", 25);
	  }

	  function get333_3genRUL_scramble(){
	  	return megascramble("3gen_L", 25);
	  }

	  function get333_3genRrU_scramble(){
	  	return megascramble("RrU", 25);
	  }

	  function get333_halfTurns_scramble(){
	  	return megascramble("half", 25);
	  }

	  function getSkewbULRBScramble(){
	  	return megascramble("skb", 25);
	  }

	  function get332scramble(){
	  	return megascramble("233", 25);
	  }

	  function get334scramble(){
	  	return megascramble("334", 40);
	  }

	  function get336scramble(){
	  	return megascramble("336", 40);
	  }

	  function get335scramble(n){
	  	return formatScramble("335", n);
	  }

 	  function get337scramble(n){
	  	return formatScramble("337", n);
	  }

 	  function get112scramble(){
	  	return megascramble("112", 25);
	  }

 	  function get888scramble(n){
	  	return megascramble("888", n);
	  }

 	  function get999scramble(n){
	  	return megascramble("999", n);
	  }

 	  function get101010scramble(n){
	  	return megascramble("101010", n);
	  }

 	  function get111111scramble(n){
	  	return megascramble("111111", n);
	  }

 	  function getSuperFloppyScramble(){
	  	return megascramble("sfl", 25);
	  }

	  return {
	    get444WCAScramble: get444WCAScramble,
	    get444SiGNScramble: get444SiGNScramble,
	    get444edgesScramble: get444edgesScramble,

	    get555WCAScramble: get555WCAScramble,
	    get555SiGNScramble: get555SiGNScramble,
	    get555edgesScramble: get555edgesScramble,

	    get666WCAScramble: get666WCAScramble,
	    get666SiGNScramble: get666SiGNScramble,
	    get666edgesScramble: get666edgesScramble,

	    get777WCAScramble: get777WCAScramble,
	    get777SiGNScramble: get777SiGNScramble,
	    get777edgesScramble: get777edgesScramble,

	    get333_2genRU_scramble: get333_2genRU_scramble,
	    get333_2genLU_scramble: get333_2genLU_scramble,
	    get333_2genMU_scramble: get333_2genMU_scramble,
	    get333_3genFRU_scramble: get333_3genFRU_scramble,
	    get333_3genRUL_scramble: get333_3genRUL_scramble,
	    get333_3genRrU_scramble: get333_3genRrU_scramble,
	    get333_halfTurns_scramble: get333_halfTurns_scramble,

	    getSkewbULRBScramble: getSkewbULRBScramble,

	    get332scramble: get332scramble,
	    get334scramble: get334scramble,
	    get336scramble: get336scramble,
	    get335scramble: get335scramble,
	    get337scramble: get337scramble,
	    get112scramble: get112scramble,
	    getSuperFloppyScramble: getSuperFloppyScramble,

	    get888scramble: get888scramble,
	    get999scramble: get999scramble,
	    get101010scramble: get101010scramble,
	    get111111scramble: get111111scramble,
	  }

})(scramble.mega, mathlib.rn, mathlib.rndEl);