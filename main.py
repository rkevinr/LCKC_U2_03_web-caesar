#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

from caesarbase import encrypt, rotate_character, alphabet_position


def build_page(message_content):
    page_heading = '<h2>Web Caesar</h2>'


    form_content =  \
        '<form method="post">' + \
        '  <textarea name="message" style="height: 100px; width: 400px;">' + \
        message_content + \
        '  </textarea>' + \
        '  <br>' + \
        '  <input type="submit">' + \
        '</form>'

    return form_content


class MainHandler(webapp2.RequestHandler):
    def get(self):
        basic_page = build_page("")
        self.response.write(basic_page)

    def post(self):
        message = self.request.get("message")
        # rotation_amount = self.request.get("
        encrypted_msg = encrypt(message, 5)
        escaped_msg = cgi.escape(encrypted_msg)
        basic_page = build_page(escaped_msg)
        self.response.write(basic_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
