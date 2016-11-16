var chats = Store.Chat.models;

var r = [];

for (i in chats){
	if(i>20)
		break;
	if(isNaN(i))
		continue;
	var chat = {};
	chat.name = chats[i]._values.formattedTitle;
	chat.messages = [];
	var messages = chats[i].msgs.models;
	var l = messages.length;
	for(var k=0;k<l;k++){
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
	
	if(chat.messages.length)
		r.push(chat);
}

return r;