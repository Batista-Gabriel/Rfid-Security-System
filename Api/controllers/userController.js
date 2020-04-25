const http = require('http');
const db = require('../connection')
const card = require('./cardController')

module.exports={

    async create(req,res){
        
        const {user_name,card_id_fk,user_nickname =user_name,user_gender}=req.body;
        const a=
        await db
        .select("user_nickname")
        .from('user')
        .innerJoin('card','card_id_fk','card_id')
        .where({card_id:card_id_fk})
        if(a.length==0){
            await db
            .insert({
                user_name,
                card_id_fk,
                user_nickname,
                user_gender
            }).into('user');
            res.json({success:true});
        }else{
            res.json({success:false})
        }
    },
    
    async index (req,res){
        await db
        .select()
        .from('user')
        .then(function(data){
            res.send(data);
        });
    },

    async user(req,res){
        await db
        .select()
        .from('user')
        .where({user_id: req.params.id})
        .then(function(data){
            res.send(data)
        });
    },

    async search(req,res){
        var [userName]=req.params.userName
        userName='%'.concat(userName,'%') 
        await db
        .select()
        .where('user_name','like',userName )
        .from('user')
        .orderBy('user_name')
        .then(function(data){
            res.send(data)
        });
    },

    async patch(req,res){
        await db
        .update(req.body)
        .from('user')
        .where({user_id:req.params.id})
        .then(function(data){
            res.json({sucess:true});
        });
    },
    async delete(req,res){
        await db
        .from('user')
        .where({user_id:req.params.id})
        .del()
        .then(function(data){
            res.json({sucess:true});
        });
    }

}
