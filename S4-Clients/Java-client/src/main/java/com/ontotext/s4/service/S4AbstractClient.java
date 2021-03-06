/*
 * S4 Java client library
 * Copyright 2016 Ontotext AD
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.ontotext.s4.service;


public interface S4AbstractClient {

    /**
     * Enables or disables the compression of the data exchanged with the S4 services
     * 
     * @param requestCompression if set to true, the data encoding is set to gzip
     */
    void setRequestCompression(boolean requestCompression);
}
