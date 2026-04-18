from flask import jsonify
#funcao resp_sucess e recebe o parametro data, message, status

def resp_sucess(data=None, message="", status=200): 
    return jsonify({
        "success": True,
        "data": data,
        "message": message
    }), status

def resp_erro(error="", status=400):
    return jsonify({
        "success": False,
        "error": error
    }), status
