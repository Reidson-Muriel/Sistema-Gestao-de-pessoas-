from flask import jsonify
#funcao resp_sucess e recebe o parametro data, message, status

def resp_sucess(message="", status=200): 
    return jsonify({
        "success": True,
        "message": message
    }), status

def resp_erro(message="", status=400):
    return jsonify({
        "success": False,
        "message": message
    }), status
