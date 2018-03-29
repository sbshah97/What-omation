var chats = Store.Chat.models;

var r = [];

for (i in chats){
	if(isNaN(i))
		continue;
	
		var chat = {};
	chat.name = chats[i]._values.formattedTitle;
	chat.messages = [];
	
	var messages = chats[i].msgs.models;
	var unread_count = chats[i]._values.unreadCount;
	var l = messages.length;
	
	if(chat.name==currentChat){
		for(var k=l-1;k>=0;k--){
			if(messages[k]._values.t <= last_seen || (messages[k].id.fromMe==true && messages[k]._values.body[0] != "\\"))
					break;
			var s;
			if(messages[k]._values.type=='chat')
				s = messages[k]._values.body;
			else
				s = '['+messages[k]._values.type.toUpperCase()+']';
			chat.messages.push(
			{
				msg: s,
				t:   messages[k]._values.t
			});
		}
		chat.messages.reverse();
	}
	else{
		for(var k=l-unread_count;k<l;k++){
			var s;
			if(messages[k]._values.type=='chat')
				s = messages[k]._values.body;
			else
				s = '['+messages[k]._values.type.toUpperCase()+']';
			chat.messages.push(
			{
				msg: s,
				t:   messages[k]._values.t
			});
		}
	}
	
	if(chat.messages.length)
		r.push(chat);
}

return r;