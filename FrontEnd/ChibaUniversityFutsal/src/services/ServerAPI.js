/**
 * 出席管理APIを呼び出すクラス
 */
export default class ServerAPI {
    /**
     * @param {string} baseURL - APIのベースURL
     */
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    /**
     * HTTPリクエストを行うヘルパーメソッド
     * @private
     * @param {string} method - HTTPメソッド
     * @param {string} uri - リクエストのURI
     * @param {Object} data - 送信するデータ
     * @returns {Promise<Object>} レスポンスデータ
     */
    async _request(method, uri, data) {
        const formData = new FormData();
        for (const key in data) {
            formData.append(key, data[key]);
        }

        const response = await fetch(`${this.baseURL}${uri}`, {
            method: method,
            body: formData
        });
        return response.json();
    }

    /**
     * 出欠登録情報の確認
     * @param {number} id_children - 園児のID
     * @param {string} date - 日付
     * @returns {Promise<Object>} 出欠情報
     */
    async getChildAttendance(id_children, date) {
        return this._request('GET', `/api/children/reserve?id_children=${id_children}&date=${date}`);
    }

    /**
     * 出欠の登録
     * @param {number} id_children - 園児のID
     * @param {string} date - 日付
     * @param {boolean} submit_attendance - 出欠情報
     * @param {string} reason - 欠席理由
     * @returns {Promise<Object>} 登録結果
     */
    async registerChildAttendance(id_children, date, submit_attendance, reason) {
        return this._request('POST', `/api/children/reserve?id_children=${id_children}&date=${date}`, {
            submit_attendance,
            reason
        });
    }

    /**
     * 出欠の登録情報を更新する
     * @param {number} id_children - 園児のID
     * @param {string} date - 日付
     * @param {boolean} submit_attendance - 出欠情報
     * @param {string} reason - 欠席理由
     * @returns {Promise<Object>} 更新結果
     */
    async updateChildAttendance(id_children, date, submit_attendance, reason) {
        return this._request('PUT', `/api/children/reserve?id_children=${id_children}&date=${date}`, {
            submit_attendance,
            reason
        });
    }

    /**
     * 出欠の登録情報を検索する
     * @param {number} id_children - 園児のID
     * @param {string} date - 日付
     * @returns {Promise<Object>} 検索結果
     */
    async searchTeacherAttendance(id_children, date) {
        return this._request('GET', `/api/teachers/reserve?id_children=${id_children}&date=${date}`);
    }

    /**
     * 出欠を登録する
     * @param {number} id_children - 園児のID
     * @param {string} date - 日付
     * @param {boolean} submit_attendance - 出欠情報
     * @param {string} reason - 欠席理由
     * @returns {Promise<Object>} 登録結果
     */
    async registerTeacherAttendance(id_children, date, submit_attendance, reason) {
        return this._request('POST', `/api/teachers/reserve?id_children=${id_children}&date=${date}`, {
            submit_attendance,
            reason
        });
    }

    /**
     * 欠席理由への既読チェック、返信
     * @param {number} id_children - 園児のID
     * @param {string} date - 日付
     * @param {boolean} submit_attendance - 出欠情報
     * @param {string} reply_to_reason - 返信内容
     * @returns {Promise<Object>} 返信結果
     */
    async replyToReason(id_children, date, submit_attendance, reply_to_reason) {
        return this._request('PUT', `/api/teachers/reserve?id_children=${id_children}&date=${date}`, {
            submit_attendance,
            reply_to_reason
        });
    }
}

/**以下は呼び出し側での使用例 */
/*
import ServerAPI from './path/to/ServerAPI.js';



const api = new AttendanceAPI('http://127.0.0.1:5000');

api.registerChildAttendance(1, '2023_08_25', true, 'TEST')
.then(data => console.log(data));

*/



