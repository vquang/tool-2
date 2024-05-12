// global var
let listFile = []
let feature = 0
let option = 0
check()
/////////////////////////

function change(f) {
    feature = f
    check()
}

function scanApi() {
    if(feature === 0) {
        malApi()
    } else if(feature === 1) {
        logApi()
    }
}

function malApi() {
  feature = 0
  check()
  clear()
  document.querySelector('.screen-log').style.display = 'none'
  document.querySelector('.screen-mal').style.display = 'flex'
  listFile.forEach(file => {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
  
    const raw = JSON.stringify({
        "data": file
    });
  
    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };
  
    fetch("http://localhost:5000/scan", requestOptions)
    .then((response) => response.json())
    .then((result) => {
      console.log(result['severity'])
      fillScreenMal(result)
    })
  })
}

function logApi() {
    feature = 1
    check()
    clear()
    document.querySelector('.screen-mal').style.display = 'none'
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
  
    const requestOptions = {
        method: "GET",
        headers: myHeaders,
        redirect: "follow"
    };
  
    fetch("http://localhost:5000/analyze", requestOptions)
    .then((response) => response.json())
    .then((data) => {
        // hideSpending()
        document.querySelector('.screen-log').style.display = 'flex'
        sqliApi()
    })
}

function sqliApi() {
    option = 0
    check()
    clear()
    document.querySelector('.screen-mal').style.display = 'none'
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
  
    const requestOptions = {
        method: "GET",
        headers: myHeaders,
        redirect: "follow"
    };
  
    fetch("http://localhost:5000/sqli", requestOptions)
    .then((response) => response.json())
    .then((data) => {
        // hideSpending()
        document.querySelector('.screen-log').style.display = 'flex'
        fillScreenLog(data)
    })
}

function xssApi() {
    option = 1
    check()
    clear()
    document.querySelector('.screen-mal').style.display = 'none'
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
  
    const requestOptions = {
        method: "GET",
        headers: myHeaders,
        redirect: "follow"
    };
  
    fetch("http://localhost:5000/xss", requestOptions)
    .then((response) => response.json())
    .then((data) => {
        // hideSpending()
        document.querySelector('.screen-log').style.display = 'flex'
        fillScreenLog(data)
    })
}

function cmdiApi() {
    option = 2
    check()
    clear()
    document.querySelector('.screen-mal').style.display = 'none'
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
  
    const requestOptions = {
        method: "GET",
        headers: myHeaders,
        redirect: "follow"
    };
  
    fetch("http://localhost:5000/cmdi", requestOptions)
    .then((response) => response.json())
    .then((data) => {
        // hideSpending()
        document.querySelector('.screen-log').style.display = 'flex'
        fillScreenLog(data)
    })
}

function pathTraversalApi() {
    option = 3
    check()
    clear()
    document.querySelector('.screen-mal').style.display = 'none'
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
  
    const requestOptions = {
        method: "GET",
        headers: myHeaders,
        redirect: "follow"
    };
  
    fetch("http://localhost:5000/path-traversal", requestOptions)
    .then((response) => response.json())
    .then((data) => {
        // hideSpending()
        document.querySelector('.screen-log').style.display = 'flex'
        fillScreenLog(data)
    })
}

function fillScreenLog(data) {
    let log = data['logs']
    let screen = document.querySelector('.screen-log')
    let index = 0
    log.forEach(l => {
        index++
        const div = document.createElement('div');
        div.innerHTML = `<div style="display:flex;"><p style="color:#ff0066;font-weight:bold">${index}</p>: ${l}</div>`
        screen.appendChild(div)
    })
}

function fillScreenMal(data) {
    let mal = data['data']
    let screen = document.querySelector('.screen-mal')
    let severity = mal['severity']
    const div = document.createElement('div');
    div.classList.add('mal-item')
    div.innerHTML = `<div class="up">
                        <div class="mal-left">${mal['filePath']}</div>
                        </div>
                        <div class="down ${severity}">
                        <div class="mal-left">${mal['malwareType']}</div>
                        <div class="mal-right">
                            <i class="fa-solid fa-triangle-exclamation"></i>
                        </div>
                    </div>`
    screen.append(div)
}

function clear() {
    document.querySelector('.screen-mal').innerHTML = ''
    document.querySelector('.screen-log').innerHTML = ''
}



document.querySelector('.choose-file').addEventListener('change', function(e) {
    const list = []
    const obj = e.target.files;
    for(i = 0; i < obj.length; ++i) {
        list.push(obj[i].path)
    }
    listFile = list
});

function check() {
    let mal = document.querySelector('.h-left-mal')
    let log = document.querySelector('.h-left-log')
    let op0 = document.querySelector('.op-0')
    let op1 = document.querySelector('.op-1')
    let op2 = document.querySelector('.op-2')
    let op3 = document.querySelector('.op-3')

    op0.classList.remove('active');
    op1.classList.remove('active');
    op2.classList.remove('active');
    op3.classList.remove('active');

    let slog = document.querySelector('.screen-log')
    let opF = document.querySelector('.op-frame')
    let choose = document.querySelector('.choose-file')
    let sMal = document.querySelector('.screen-mal')

    if(feature === 0) {
        mal.classList.add('active');
        log.classList.remove('active');
        slog.style.display = 'none'
        opF.style.display = 'none'
        choose.style.display = 'flex'
    } else if(feature === 1) {
        mal.classList.remove('active');
        log.classList.add('active');
        choose.style.display = 'none'
        sMal.style.display = 'none'
        opF.style.display = 'flex'
    }

    if(option === 0) {
        op0.classList.add('active')
    } else if(option === 1) {
        op1.classList.add('active')
    } else if(option === 2) {
        op2.classList.add('active')
    } else {
        op3.classList.add('active')
    }
}