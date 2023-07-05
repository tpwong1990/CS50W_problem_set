document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => {load_mailbox('inbox')});
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  
  
  // By default, load the inbox
  load_mailbox('inbox');
  });
  
  function compose_email() {
  
      // Show compose view and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'block';
      document.querySelector('#click-view').style.display = 'none';
  
      // Clear out composition fields
      document.querySelector('#compose-recipients').value = '';
      document.querySelector('#compose-subject').value = '';
      document.querySelector('#compose-body').value = '';
  }
  
  function create_email_table(id, subject, sender, receiver, timestamp, read_status, body, detail, mailbox, archived) {
  
      // Create div for email
      email_div = document.createElement('div');
      if (detail == false) {
          email_div.id = `list_${id}`;
          email_div.className = `${mailbox}_list`;
      } else {
          email_div.className = 'detail_box';
      }
  
      // Style the div
      email_div.style.border = "thin solid #000000";
      email_div.style.margin = "3px";
      email_div.style.padding = "3px";
      if (detail == false) {
          if (read_status == false) {
              email_div.style.backgroundColor = "white" 
          } else {
              email_div.style.backgroundColor = "gray" 
          };
      };
  
      // Insert the div into emails-view div
      if (detail == false) {
          const view_div = document.getElementById('emails-view');
          view_div.appendChild(email_div);
      } else {
          const view_div = document.getElementById('click-view');
          view_div.appendChild(email_div);
      };
      
  
      // Create table 
      table = document.createElement('table');
      if (detail == false) {
          document.getElementById(`list_${id}`).appendChild(table);
      } else {
          document.querySelector('.detail_box').appendChild(table);
      }
  
      // Insert table cell
      var r, c;
      if (detail == false) {
          r = table.insertRow(0);
          c = r.insertCell(0);
          c.innerHTML = '<strong>Subject:</strong>'
          c = r.insertCell(1);
          c.innerHTML = subject;
          r = table.insertRow(1);
          c =r.insertCell(0);
          c.innerHTML = '<strong>From:</strong>';
          c =r.insertCell(1);
          c.innerHTML = sender;
          r = table.insertRow(2);
          c = r.insertCell(0);
          c.innerHTML = '<strong>Time:</strong>';
          c = r.insertCell(1);
          c.innerHTML = timestamp;
          r = table.insertRow(3);
      } else {
          var r, c;
          r = table.insertRow(0);
          c = r.insertCell(0);
          c.innerHTML = '<strong>From:</strong>';
          c = r.insertCell(1);
          c.innerHTML = sender;
          r = table.insertRow(1);
          c = r.insertCell(0);
          c.innerHTML = '<strong>Subject:</strong>';
          c = r.insertCell(1);
          c.innerHTML = subject;
          r = table.insertRow(2);
          c = r.insertCell(0);
          c.innerHTML = '<strong>To:</strong>';
          c = r.insertCell(1);
          c.innerHTML = receiver;
          r = table.insertRow(3);
          c = r.insertCell(0);
          c.innerHTML = 'Time:';
          c = r.insertCell(1);
          c.innerHTML = timestamp;
          r = table.insertRow(4);
          c = r.insertCell(0);
          c.innerHTML = '<strong>Message:</strong>';
          c = r.insertCell(1);
          c.innerHTML = `<textarea disabled rows="2" cols="100" style="resize:none; width: 100%; min-height:300px;">${body}</textarea>`
          r = table.insertRow(5);
          if (mailbox === 'inbox' || mailbox === 'archive') {
              c = r.insertCell(0);
              if (archived == true) {
                  c.innerHTML = `<button id="unarchive" value=${id}>Unarchive</button>`;
                  document.querySelector('#unarchive').addEventListener('click', function(event) {
                      const button = event.target;
                      const email_id = button.value;
                      unarchive_email(email_id);
                  });
              } else {
                  c.innerHTML = `<button id="archive" value=${id}>Archive</button>`;
                  document.querySelector('#archive').addEventListener('click', function(event) {
                      const button = event.target;
                      const email_id = button.value
                      archive_email(email_id);
                  });
              };
          };
          r = table.insertRow(6);
          c = r.insertCell(0);
          c.innerHTML = `<button id="rely" value=${id} >Rely</button>`
          document.querySelector('#rely').addEventListener('click', function(event) {
              const button = event.target;
              const email_id = button.value
              rely_email(email_id);
              });
      };
  };
  
  
  function load_mailbox(mailbox) {
  
      // Show the mailbox and hide other views
      document.querySelector('#emails-view').style.display = 'block';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#click-view').style.display = 'none';
  
      // Show the mailbox name
      document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
      //Show mailbox content
      fetch(`/emails/${mailbox}`)
      .then(response => response.json())
      .then(emails => {
          emails.forEach(element => {
          const subject = element['subject'];
  
          // need to handle mulit recipents
          const receiver = element['recipients'];
  
          const sender = element['sender'];
          const id =  element['id'];
          const timestamp = element['timestamp'];
          const read_status = element['read'];
          const detail = false;
          const body = '';
          const archive = element['archived'];
          let sent_mailbox = false;
          if (mailbox === 'sent') {
              sent_mailbox = true;
          }
  
  
          create_email_table(id, subject, sender, receiver, timestamp, read_status, body, detail, mailbox, archive)
          });  
      });
  }
  
  // Send the email
  document.addEventListener('DOMContentLoaded', function() {
      document.querySelector('#compose-form').addEventListener("submit", () => {
          const receiver = document.querySelector('#compose-recipients').value;
          const mail_subject = document.querySelector('#compose-subject').value;
          const mail_body = document.querySelector('#compose-body').value;
          //console.log(receiver);
          //console.log(mail_subject);
          //console.log(mail_body);
  
          // Post eamil
          fetch('/emails', {
              method: 'POST',
              body: JSON.stringify({
                  recipients: receiver,
                  subject: mail_subject,
                  body: mail_body
              })
          })
          .then(response => response.json())
          .then(result => {
              // Print result
              //console.log(result);
           });
  
           // Show sent mail box after email sent
           setTimeout(() => {  load_mailbox('sent'); }, 300);
  
           // stop the form to be submitted
           event.returnValue = false;
      });
  })
  
  // Click email
  document.addEventListener('DOMContentLoaded', function() {
      document.addEventListener('click', event => {
          const element = event.target;
          // check which email box is click
          if (element.className === 'inbox_list' || element.className === 'sent_list' || element.className === 'archive_list') {
              const id_string = element.id;
              const tempArray = id_string.split("_");
              const id = tempArray[1]; 
              //console.log(id)
              // show email details view
              document.querySelector('#emails-view').style.display = 'none';
              document.querySelector('#compose-view').style.display = 'none';
              document.querySelector('#click-view').style.display = 'block';
  
              // clean the content on div
              document.querySelector('#click-view').innerHTML='';
              
              // get email detail
              fetch(`/emails/${id}`)
              .then(response => response.json())
              .then(email => {
                  // Print email
                  //console.log(email);
              
                  //console.log('a');
                  // render email details
                  const detail = true;
                  let mailbox;
                  if (element.className === 'inbox_list'){
                      mailbox = 'inbox';
                  }
                  if (element.className === 'sent_list'){
                      mailbox = 'sent';
                  }
                  if (element.className === 'archive_list'){
                      mailbox = 'archive';
                  }
  
                  create_email_table(email['id'], email['subject'], email['sender'], email['recipients'], email['timestamp'], email['read'], email['body'], detail, mailbox, email['archived']);
  
                  // change the read status
                  fetch(`/emails/${id}`, {
                      method: 'PUT',
                      body: JSON.stringify({
                          read: true
                      })
                  });
              });
          }
      });
  });
  
  function archive_email(id){
      fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: true
          })
      })
      setTimeout(() => { load_mailbox('inbox');}, 300);
  }
  
  function unarchive_email(id){
      fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: false
          })
      })
      setTimeout(() => { load_mailbox('inbox');},300);
  }
  
  function rely_email(id){
      fetch(`/emails/${id}`)
          .then(response => response.json())
          .then(email => {
              const sender = email['sender'];
              const subject = email['subject'];
              const time = email['timestamp'];
              const body = email['body'];
  
              // Pre-fill composition fields
              document.querySelector('#compose-recipients').value = sender;
              let new_subject;
              if (subject.indexOf('Re:') == 0){
                  new_subject = subject;
              } else {
                  new_subject = "Re: " + subject;
              }
              
              document.querySelector('#compose-subject').value = new_subject;
              //var today = new Date();
              const monthNames = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"
              ];
              //var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
              //console.log(time);
              document.querySelector('#compose-body').value = 'On ' + time + ', ' + sender + ' wrote: ' + body;
          });
  
      // Show compose view and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'block';
      document.querySelector('#click-view').style.display = 'none';
  
  };
  