{
    "targets": [{
        "target_name":
        "index",
        "sources": ["index.cc"],
        "cflags!": ["-fno-exceptions"],
        "cflags_cc!": ["-fno-exceptions"],
        "default_configuration":
        "Release",
        "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
            "CLANG_CXX_LIBRARY": "libc++",
            "MACOSX_DEPLOYMENT_TARGET": "10.7",
        },
        "msvs_settings": {
            "VCCLCompilerTool": {
                "ExceptionHandling": 1
            },
        },
        "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
        "include_dirs": ["<!@(node -p \"require('node-addon-api').include\")"],
        "conditions": [[
            "OS=='mac'",
            {
                "cflags+": ["-fvisibility=hidden"],
                "xcode_settings": {
                    "GCC_SYMBOLS_PRIVATE_EXTERN": "YES",  # -fvisibility=hidden
                }
            }
        ]],
    }]
}
