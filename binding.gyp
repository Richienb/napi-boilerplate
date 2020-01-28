{
    "targets": [{
        "target_name":
        "<(module_name)",
        "sources": ["index.cc"],
        "cflags!": ["-fno-exceptions"],
        "cflags_cc!": ["-fno-exceptions"],
        "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
        "conditions": [[
            'OS=="win"', {
                "msvs_settings": {
                    "VCCLCompilerTool": {
                        "ExceptionHandling": 1
                    }
                }
            }
        ],
                       [
                           'OS=="mac"', {
                               "xcode_settings": {
                                   "CLANG_CXX_LIBRARY": "libc++",
                                   "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                                   "MACOSX_DEPLOYMENT_TARGET": "10.7"
                               }
                           }
                       ]],
        "include_dirs": [
            "<!@(node -p \"require('node-addon-api').include\")",
            "node_modules/node-addon-api",
            "node_modules/node-addon-api/external-napi"
        ],
        "defines": ["NAPI_VERSION=<(napi_build_version)"]
    }, {
        "target_name":
        "action_after_build",
        "type":
        "none",
        "dependencies": ["<(module_name)"],
        "copies": [{
            "files": ["<(PRODUCT_DIR)/<(module_name).node"],
            "destination": "<(module_path)"
        }],
        "cflags!": ["-fno-exceptions"],
        "cflags_cc!": ["-fno-exceptions"],
        "conditions": [[
            'OS=="win"', {
                "msvs_settings": {
                    "VCCLCompilerTool": {
                        "ExceptionHandling": 1
                    }
                }
            }
        ],
                       [
                           'OS=="mac"', {
                               "xcode_settings": {
                                   "CLANG_CXX_LIBRARY": "libc++",
                                   "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                                   "MACOSX_DEPLOYMENT_TARGET": "10.7"
                               }
                           }
                       ]],
        "include_dirs": [
            "<!@(node -p \"require('node-addon-api').include\")",
            "node_modules/node-addon-api",
            "node_modules/node-addon-api/external-napi"
        ],
        "defines": ["NAPI_VERSION=<(napi_build_version)"]
    }]
}
